import tempfile
import unittest
from pathlib import Path

from bs4 import BeautifulSoup

from tools.medium_export import find_uncovered_tables, render_article, update_site_index


class MediumExportTests(unittest.TestCase):
    def test_article_typography_is_embedded_in_document_head(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_dir:
            root = Path(temporary_dir)
            source_path = root / "article.md"
            source_path.write_text("# Example\n\nArticle body.", encoding="utf-8")

            output_path = render_article(source_path, root / "output")
            soup = BeautifulSoup(output_path.read_text(encoding="utf-8"), "html.parser")

            self.assertEqual(len(soup.head.find_all("style")), 1)
            self.assertEqual(
                soup.head.style.string,
                """body {
    font-family: Charter, Georgia, serif;
    font-size: 21px;
    line-height: 1.65;
    color: #242424;
    max-width: 680px;
}

h1, h2, h3 {
    font-family: Inter, Helvetica, Arial, sans-serif;
    font-weight: 700;
}

pre {
    background: #f6f8fa;
    border: 1px solid #e1e4e8;
    border-radius: 8px;
    padding: 1rem;
    overflow-x: auto;
    margin: 1.5rem 0;
}

pre, code {
    font-family: "SF Mono", Consolas, Monaco, monospace;
    font-size: 0.9em;
}

pre code {
    background: none;
    padding: 0;
    font-size: inherit;
}
""",
            )
            self.assertIsNone(soup.article.find("style"))
            self.assertEqual(soup.article.p.get_text(), "Article body.")

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
            self.assertEqual(
                soup.article.find_all("h1")[0].get_text(),
                "The enhanced medallion architecture",
            )
            self.assertEqual(len(soup.article.find_all("h1")), 1)
            self.assertEqual(soup.article.contents[0].name, "h1")
            self.assertEqual(soup.article.p.get_text(), "Article body.")

    def test_frontmatter_is_removed_before_title_extraction(self) -> None:
        markdown_source = '''---
title: The enhanced medallion architecture
tags:
  - data warehouse
---

**01.** The enhanced medallion architecture

*Opening paragraph.*
'''

        with tempfile.TemporaryDirectory() as temporary_dir:
            root = Path(temporary_dir)
            source_path = root / "article.md"
            source_path.write_text(markdown_source, encoding="utf-8")

            output_path = render_article(source_path, root / "output")
            soup = BeautifulSoup(output_path.read_text(encoding="utf-8"), "html.parser")
            expected_title = "The enhanced medallion architecture"

            self.assertEqual(soup.title.get_text(), expected_title)
            self.assertEqual(soup.article.h1.get_text(), expected_title)
            self.assertEqual(len(soup.article.find_all("h1")), 1)
            self.assertNotIn("title: The enhanced medallion architecture", soup.article.get_text())
            self.assertEqual(soup.article.p.get_text(), "Opening paragraph.")

    def test_markdown_title_is_visible_once_and_matches_metadata(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_dir:
            root = Path(temporary_dir)
            source_path = root / "article.md"
            source_path.write_text(
                "# The Journey to an AI-Ready Data Warehouse\n\nArticle body.\n\n"
                "## Architecture\n\nMore content.",
                encoding="utf-8",
            )

            output_path = render_article(source_path, root / "output")
            soup = BeautifulSoup(output_path.read_text(encoding="utf-8"), "html.parser")
            title = "The Journey to an AI-Ready Data Warehouse"

            self.assertEqual(soup.title.get_text(), title)
            self.assertEqual(soup.find("meta", property="og:title")["content"], title)
            self.assertEqual(len(soup.article.find_all("h1")), 1)
            self.assertEqual(soup.article.contents[0].name, "h1")
            self.assertEqual(soup.article.h1.get_text(), title)
            self.assertEqual(soup.article.get_text().count(title), 1)
            self.assertEqual(soup.article.p.get_text(), "Article body.")
            self.assertEqual(soup.article.h2.get_text(), "Architecture")

    def test_visible_title_is_escaped_and_normalized(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_dir:
            root = Path(temporary_dir)
            source_path = root / "article.md"
            source_path.write_text(
                "# 01. Research & Development &lt;Target&gt;\n\nArticle body.",
                encoding="utf-8",
            )

            output_path = render_article(source_path, root / "output")
            soup = BeautifulSoup(output_path.read_text(encoding="utf-8"), "html.parser")
            title = "Research & Development <Target>"

            self.assertEqual(soup.article.h1.get_text(), title)
            self.assertEqual(soup.title.get_text(), title)
            self.assertIsNone(soup.article.h1.find("target"))
            self.assertIn("&lt;Target&gt;", str(soup.article.h1))

    def test_filename_title_is_visible_when_no_title_node_exists(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_dir:
            root = Path(temporary_dir)
            source_path = root / "article.md"
            source_path.write_text("## Architecture", encoding="utf-8")

            output_path = render_article(source_path, root / "output")
            soup = BeautifulSoup(output_path.read_text(encoding="utf-8"), "html.parser")

            self.assertEqual(soup.article.h1.get_text(), "article")
            self.assertEqual(soup.title.get_text(), "article")
            self.assertEqual(soup.article.h2.get_text(), "Architecture")

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
                block.get_text(separator="\n"),
                'if amount < 100:\n    print("review")',
            )
            self.assertEqual(len(block.find_all("br")), 1)
            self.assertEqual(len(soup.find_all("pre")), 1)
            self.assertEqual(str(block.contents[-1]), '    print("review")')
            self.assertIn("amount &lt; 100", html)
            self.assertEqual(soup.p.code.get_text(), "amount")

    def test_code_line_breaks_preserve_blank_lines_indentation_and_language(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_dir:
            root = Path(temporary_dir)
            source_path = root / "article.md"
            lines = ["select", "    a.[id],", "", "", "    '<tag>&' as value", "from source"]
            for language in ("sql", "yaml", ""):
                with self.subTest(language=language):
                    source_path.write_text(
                        f"# Example\n\n```{language}\n" + "\n".join(lines) + "\n```\n",
                        encoding="utf-8",
                    )
                    output_path = render_article(source_path, root / "output")
                    soup = BeautifulSoup(output_path.read_text(encoding="utf-8"), "html.parser")
                    blocks = soup.find_all("pre")

                    self.assertEqual(len(blocks), 1)
                    block = blocks[0]
                    self.assertEqual(block["data-code-block-lang"], language or "text")
                    self.assertEqual(len(block.find_all("br")), len(lines) - 1)
                    self.assertEqual(
                        "".join("\n" if child.name == "br" else str(child) for child in block.contents),
                        "\n".join(lines),
                    )
                    self.assertIsNone(block.find("tag"))
                    self.assertFalse(str(block).endswith("<br/></pre>"))

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

    def test_medium_exclusion_markers_remove_marked_content_from_export(self) -> None:
        markdown_source = '''# Example

![Layer contracts](assets/layer-contracts.png)

<!-- MEDIUM:EXCLUDE:START -->
| Layer | Owns |
|---|---|
| Bronze | Source fidelity |
<!-- MEDIUM:EXCLUDE:END -->

This paragraph remains in the exported article.
'''

        with tempfile.TemporaryDirectory() as temporary_dir:
            root = Path(temporary_dir)
            source_path = root / "article.md"
            asset_path = root / "assets" / "layer-contracts.png"
            asset_path.parent.mkdir()
            asset_path.write_bytes(b"image")
            source_path.write_text(markdown_source, encoding="utf-8")

            output_path = render_article(source_path, root / "output")
            soup = BeautifulSoup(output_path.read_text(encoding="utf-8"), "html.parser")
            exported_html = output_path.read_text(encoding="utf-8")

            self.assertEqual(len(soup.find_all("table")), 0)
            self.assertIsNotNone(soup.find("img", alt="Layer contracts"))
            self.assertIn("This paragraph remains in the exported article.", soup.get_text())
            self.assertNotIn("MEDIUM:EXCLUDE", exported_html)
            self.assertIn("| Layer | Owns |", source_path.read_text(encoding="utf-8"))

    def test_unmatched_medium_exclusion_marker_is_an_error(self) -> None:
        markdown_source = '''# Example

<!-- MEDIUM:EXCLUDE:START -->
This content must not leak into the export.
'''

        with tempfile.TemporaryDirectory() as temporary_dir:
            root = Path(temporary_dir)
            source_path = root / "article.md"
            source_path.write_text(markdown_source, encoding="utf-8")

            with self.assertRaisesRegex(ValueError, "Unmatched MEDIUM:EXCLUDE marker"):
                render_article(source_path, root / "output")

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