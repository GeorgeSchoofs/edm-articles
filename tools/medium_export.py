"""Export an article Markdown file as Medium-importable static HTML."""

from __future__ import annotations

import argparse
import html
import re
import shutil
from pathlib import Path
from urllib.parse import unquote, urlparse

import markdown
from bs4 import BeautifulSoup, NavigableString


REVIEW_BLOCK = re.compile(
    r"<!--\s*REVIEW:START\s*-->.*?<!--\s*REVIEW:END\s*-->",
    re.DOTALL | re.IGNORECASE,
)
FRONTMATTER_BLOCK = re.compile(
    r"\A(?:\ufeff)?---[ \t]*\r?\n.*?\r?\n---[ \t]*(?:\r?\n|$)",
    re.DOTALL,
)
MEDIUM_EXCLUDE_MARKER = re.compile(
    r"<!--\s*MEDIUM:EXCLUDE:(START|END)\s*-->",
    re.IGNORECASE,
)
AUDIENCE_LINE = re.compile(
    r"^\*{0,2}Intended audience:\*{0,2}.*$", re.MULTILINE | re.IGNORECASE
)
TITLE_NUMBER = re.compile(r"^\s*\d+(?:\.\d+)*[.)]?\s*")
ARTICLE_STYLES = """body {
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
"""


def clean_article_markdown(source: str) -> str:
    """Remove editorial metadata and marked publication-only source sections."""
    source = FRONTMATTER_BLOCK.sub("", source)
    source = REVIEW_BLOCK.sub("", source)
    markers = list(MEDIUM_EXCLUDE_MARKER.finditer(source))
    if len(markers) % 2:
        raise ValueError("Unmatched MEDIUM:EXCLUDE marker in article Markdown")

    retained = []
    cursor = 0
    for start_marker, end_marker in zip(markers[::2], markers[1::2]):
        if (
            start_marker.group(1).casefold() != "start"
            or end_marker.group(1).casefold() != "end"
        ):
            raise ValueError("MEDIUM:EXCLUDE markers must be ordered START then END")
        retained.append(source[cursor : start_marker.start()])
        cursor = end_marker.end()
    retained.append(source[cursor:])
    source = "".join(retained)
    source = AUDIENCE_LINE.sub("", source)
    return source.strip()


def normalize_code_blocks(soup: BeautifulSoup) -> None:
    """Use importer-friendly pre blocks while retaining their source language."""
    for pre in soup.find_all("pre"):
        code = pre.find("code")
        content = code.get_text() if code else pre.get_text()
        classes = code.get("class", []) if code else []
        language = next(
            (item.removeprefix("language-") for item in classes if item.startswith("language-")),
            "text",
        )

        pre.clear()
        pre.attrs = {
            "class": [f"language-{language}"],
            "data-code-block-lang": language,
        }
        lines = content.removesuffix("\n").split("\n")
        for index, line in enumerate(lines):
            if index:
                pre.append(soup.new_tag("br"))
            pre.append(NavigableString(line))

    for wrapper in soup.select("div.codehilite, div.sourceCode"):
        wrapper.unwrap()


def copy_local_images(soup: BeautifulSoup, source_path: Path, output_dir: Path) -> None:
    """Copy local article images and rewrite their URLs relative to index.html."""
    image_dir = output_dir / "images"

    for image in soup.find_all("img", src=True):
        src = str(image["src"])
        parsed = urlparse(src)
        if parsed.scheme or parsed.netloc or src.startswith("//"):
            continue

        source_image = (source_path.parent / unquote(parsed.path)).resolve()
        if not source_image.is_file():
            raise FileNotFoundError(f"Referenced image not found: {source_image}")

        image_dir.mkdir(parents=True, exist_ok=True)
        destination = image_dir / source_image.name
        shutil.copy2(source_image, destination)
        image["src"] = f"images/{destination.name}"


def remove_legacy_table_images(output_dir: Path) -> None:
    """Delete artifacts created by the retired automatic table rasterizer."""
    image_dir = output_dir / "images"
    if image_dir.is_dir():
        for image_path in image_dir.glob("table-[0-9][0-9].png"):
            image_path.unlink()


def find_uncovered_tables(soup: BeautifulSoup) -> list[int]:
    """Return one-based table numbers without an immediately preceding visual."""
    uncovered = []
    for table_number, table in enumerate(soup.find_all("table"), start=1):
        previous = table.find_previous_sibling()
        if previous is None or previous.find("img") is None:
            uncovered.append(table_number)
    return uncovered


def normalize_headings(soup: BeautifulSoup) -> None:
    """Map deep Markdown headings to Medium's heading/subheading hierarchy."""
    for heading in soup.find_all(["h3", "h4", "h5", "h6"]):
        heading.name = "h2" if heading.name == "h3" else "h3"


def remove_inter_element_whitespace(soup: BeautifulSoup) -> None:
    """Prevent importers from interpreting formatting whitespace as blank blocks."""
    for node in list(soup.find_all(string=True)):
        if node.find_parent(["pre", "code"]) is not None:
            continue
        if isinstance(node, NavigableString) and not node.strip():
            node.extract()


def make_image_urls_absolute(soup: BeautifulSoup, base_url: str | None) -> None:
    if not base_url:
        return
    for image in soup.find_all("img", src=True):
        if not urlparse(str(image["src"])).scheme:
            image["src"] = f"{base_url.rstrip('/')}/{str(image['src']).lstrip('/')}"


def render_article(source_path: Path, output_dir: Path, base_url: str | None = None) -> Path:
    """Render one Markdown article to a standalone static index.html page."""
    source = clean_article_markdown(source_path.read_text(encoding="utf-8"))
    body_html = markdown.markdown(
        source,
        extensions=["fenced_code", "tables", "sane_lists"],
        output_format="html5",
    )
    body = BeautifulSoup(body_html, "html.parser")

    title_node = body.find("h1") or body.find("p")
    raw_title = title_node.get_text(" ", strip=True) if title_node else source_path.stem
    title = TITLE_NUMBER.sub("", raw_title)
    if title_node:
        title_node.decompose()

    normalize_code_blocks(body)
    normalize_headings(body)

    output_dir.mkdir(parents=True, exist_ok=True)
    remove_legacy_table_images(output_dir)
    copy_local_images(body, source_path, output_dir)
    make_image_urls_absolute(body, base_url)
    remove_inter_element_whitespace(body)

    document = BeautifulSoup("<!doctype html><html><head></head><body></body></html>", "html.parser")
    document.html["lang"] = "en"
    document.head.append(document.new_tag("meta", charset="utf-8"))
    viewport = document.new_tag("meta")
    viewport["name"] = "viewport"
    viewport["content"] = "width=device-width, initial-scale=1"
    document.head.append(viewport)
    title_element = document.new_tag("title")
    title_element.string = title
    document.head.append(title_element)
    open_graph_title = document.new_tag("meta")
    open_graph_title["property"] = "og:title"
    open_graph_title["content"] = title
    document.head.append(open_graph_title)
    style_element = document.new_tag("style")
    style_element.string = ARTICLE_STYLES
    document.head.append(style_element)

    article = document.new_tag("article")
    visible_title = document.new_tag("h1")
    visible_title.string = title
    article.append(visible_title)
    for child in list(body.contents):
        article.append(child.extract())
    document.body.append(article)

    output_path = output_dir / "index.html"
    output_path.write_text(str(document), encoding="utf-8", newline="\n")
    return output_path


def update_site_index(site_root: Path, article_slug: str, article_title: str) -> Path:
    """Create or update the publication root with one link per exported article."""
    index_path = site_root / "index.html"
    entries: dict[str, str] = {}
    if index_path.is_file():
        existing = BeautifulSoup(index_path.read_text(encoding="utf-8"), "html.parser")
        for link in existing.select("ul a[href]"):
            entries[str(link["href"])] = link.get_text(" ", strip=True)

    entries[f"{article_slug}/"] = article_title
    lines = [
        "<!doctype html>",
        '<html lang="en">',
        "<head>",
        '  <meta charset="utf-8">',
        '  <meta name="viewport" content="width=device-width, initial-scale=1">',
        "  <title>EDM Articles</title>",
        "</head>",
        "<body>",
        "  <h1>EDM Articles</h1>",
        "  <ul>",
    ]
    lines.extend(
        f'    <li><a href="{html.escape(href, quote=True)}">{html.escape(title)}</a></li>'
        for href, title in sorted(entries.items())
    )
    lines.extend(["  </ul>", "</body>", "</html>", ""])
    index_path.write_text("\n".join(lines), encoding="utf-8", newline="\n")
    return index_path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convert article Markdown to HTML suitable for Medium's URL importer."
    )
    parser.add_argument("source", type=Path, help="Markdown article to export")
    destination = parser.add_mutually_exclusive_group()
    destination.add_argument(
        "--output-dir",
        type=Path,
        help="Output directory (default: medium-site/<article filename>)",
    )
    destination.add_argument(
        "--site-root",
        type=Path,
        help="Publication repository root; creates <site-root>/<article filename>",
    )
    parser.add_argument(
        "--base-url",
        help="Public URL of the generated article, used for absolute image URLs",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    source_path = args.source.resolve()
    if not source_path.is_file():
        raise FileNotFoundError(f"Article not found: {source_path}")

    if args.output_dir:
        output_dir = args.output_dir
    elif args.site_root:
        output_dir = args.site_root / source_path.stem
    else:
        output_dir = Path("medium-site") / source_path.stem
    output_path = render_article(source_path, output_dir.resolve(), args.base_url)
    rendered = BeautifulSoup(output_path.read_text(encoding="utf-8"), "html.parser")
    uncovered_tables = find_uncovered_tables(rendered)
    if uncovered_tables:
        table_list = ", ".join(str(number) for number in uncovered_tables)
        print(
            f"WARNING: Medium will omit HTML table(s) {table_list}. "
            "Generate and insert curated infographic assets before importing."
        )
    if args.site_root:
        update_site_index(
            args.site_root.resolve(),
            source_path.stem,
            rendered.title.get_text(strip=True),
        )
    print(output_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())