import tempfile
import unittest
from pathlib import Path

from bs4 import BeautifulSoup

from tools.medium_export import find_uncovered_tables, render_article, update_site_index


class MediumExportTests(unittest.TestCase):
    def test_site_index_creates_updates_and_sorts_article_links(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_dir:
            site_root = Path(temporary_dir)

            update_site_index(site_root, "Article_01_01", "Old title")
            update_site_index(site_root, "Article_00_01", "First article")
            update_site_index(site_root, "Article_01_01", "Updated title")

            html = (site_root / "index.html").read_text(encoding="utf-8")
            soup = BeautifulSoup(html, "html.parser")
            links = [(link["href"], link.get_text()) for link in soup.select("ul a")]

            self.assertEqual(
                links,
                [
                    ("Article_00_01/", "First article"),
                    ("Article_01_01/", "Updated title"),
                ],
            )
            self.assertEqual(html.count("Article_01_01/"), 1)

    def test_first_paragraph_is_title_when_article_has_no_h1(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_dir:
            root = Path(temporary_dir)
            source_path = root / "article.md"
            source_path.write_text(
                "**01.** The enhanced medallion architecture\n\nArticle body.",
                encoding="utf-8",
            )

            output_path = render_article(source_path, root / "output")
            soup = BeautifulSoup(output_path.read_text(encoding="utf-8"), "html.parser")

            self.assertEqual(soup.title.get_text(), "The enhanced medallion architecture")
            self.assertNotIn("The enhanced medallion architecture", soup.body.get_text())

    def test_code_blocks_are_plain_semantic_html_and_escaped(self) -> None:
        markdown_source = '''# Example

```python
if amount < 100:
    print("review")
```

Use `amount` inline.
'''

        with tempfile.TemporaryDirectory() as temporary_dir:
            root = Path(temporary_dir)
            source_path = root / "article.md"
            source_path.write_text(markdown_source, encoding="utf-8")

            output_path = render_article(source_path, root / "output")
            html = output_path.read_text(encoding="utf-8")
            soup = BeautifulSoup(html, "html.parser")

            block = soup.find("pre")
            self.assertIsNotNone(block)
            self.assertEqual(block["class"], ["language-python"])
            self.assertEqual(block["data-code-block-lang"], "python")
            self.assertIsNone(block.code)
            self.assertEqual(
                block.get_text(),
                'if amount < 100:\n    print("review")\n',
            )
            self.assertIn("amount &lt; 100", html)
            self.assertEqual(soup.p.code.get_text(), "amount")

    def test_review_metadata_is_removed_and_local_images_are_copied(self) -> None:
        markdown_source = '''<!-- REVIEW:START -->
> Internal review
<!-- REVIEW:END -->

Intended audience: technical
**Intended audience:** technical

# Published title

![Diagram](assets/diagram.png)
'''

        with tempfile.TemporaryDirectory() as temporary_dir:
            root = Path(temporary_dir)
            source_path = root / "article.md"
            image_path = root / "assets" / "diagram.png"
            image_path.parent.mkdir()
            image_path.write_bytes(b"image")
            source_path.write_text(markdown_source, encoding="utf-8")

            output_path = render_article(source_path, root / "output")
            soup = BeautifulSoup(output_path.read_text(encoding="utf-8"), "html.parser")

            self.assertEqual(soup.title.get_text(), "Published title")
            self.assertNotIn("Internal review", soup.get_text())
            self.assertNotIn("Intended audience", soup.get_text())
            self.assertEqual(soup.img["src"], "images/diagram.png")
            self.assertTrue((root / "output" / "images" / "diagram.png").is_file())

    def test_figure_display_sizing_survives_export(self) -> None:
        markdown_source = '''# Example

<figure>
  <img src="assets/diagram.png" alt="Diagram description" width="700" style="max-width: 100%; height: auto;">
  <figcaption>Figure 1. Diagram caption.</figcaption>
</figure>
'''

        with tempfile.TemporaryDirectory() as temporary_dir:
            root = Path(temporary_dir)
            source_path = root / "article.md"
            image_path = root / "assets" / "diagram.png"
            image_path.parent.mkdir()
            image_path.write_bytes(b"image")
            source_path.write_text(markdown_source, encoding="utf-8")

            for base_url in (None, "https://example.com/Article_01_01/"):
                with self.subTest(base_url=base_url):
                    output_path = render_article(source_path, root / "output", base_url)
                    soup = BeautifulSoup(output_path.read_text(encoding="utf-8"), "html.parser")
                    image = soup.figure.img

                    self.assertEqual(image["width"], "700")
                    self.assertEqual(image["style"], "max-width: 100%; height: auto;")
                    self.assertNotIn("height", image.attrs)
                    self.assertEqual(image["alt"], "Diagram description")
                    expected_src = (
                        f"{base_url}images/diagram.png" if base_url else "images/diagram.png"
                    )
                    self.assertEqual(image["src"], expected_src)
                    self.assertEqual(soup.figure.figcaption.get_text(), "Figure 1. Diagram caption.")
                    self.assertEqual(
                        (root / "output" / "images" / "diagram.png").read_bytes(), b"image"
                    )

    def test_tables_remain_html_and_curated_visuals_cover_them(self) -> None:
        markdown_source = '''# Example

![Layer contracts](assets/layer-contracts.png)

| Layer | Owns |
|---|---|
| Bronze | Source fidelity |

| Source | Target |
|---|---|
| invoice | sales_invoice |
'''

        with tempfile.TemporaryDirectory() as temporary_dir:
            root = Path(temporary_dir)
            source_path = root / "article.md"
            asset_path = root / "assets" / "layer-contracts.png"
            asset_path.parent.mkdir()
            asset_path.write_bytes(b"image")
            source_path.write_text(markdown_source, encoding="utf-8")

            output_path = render_article(
                source_path,
                root / "output",
                "https://example.com/Article_01_01/",
            )
            soup = BeautifulSoup(output_path.read_text(encoding="utf-8"), "html.parser")

            self.assertEqual(len(soup.find_all("table")), 2)
            self.assertEqual(
                soup.img["src"],
                "https://example.com/Article_01_01/images/layer-contracts.png",
            )
            self.assertEqual(find_uncovered_tables(soup), [2])

    def test_headings_do_not_have_intervening_whitespace_nodes(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_dir:
            root = Path(temporary_dir)
            source_path = root / "article.md"
            source_path.write_text(
                "# Example\n\n### Bronze layer enhanced\n\nThe Bronze layer is where data lands.",
                encoding="utf-8",
            )

            output_path = render_article(source_path, root / "output")
            html = output_path.read_text(encoding="utf-8")

            self.assertIn(
                "<h2>Bronze layer enhanced</h2><p>The Bronze layer is where data lands.</p>",
                html,
            )


if __name__ == "__main__":
    unittest.main()