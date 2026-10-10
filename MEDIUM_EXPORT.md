# Medium HTML export

Install the exporter dependencies once:

```powershell
python -m pip install -r requirements-medium.txt
```

Export an article:

```powershell
python tools/medium_export.py series1/Article_01_01.md `
	--site-root ..\edm_articles_medium `
	--base-url https://georgeschoofs.github.io/edm-articles-medium/Article_01_01/
```

The command writes `../edm_articles_medium/Article_01_01/index.html`. It removes YAML
frontmatter, the internal review block, and audience line, copies local images, and converts fenced code to plain
`<pre>` markup with explicit language metadata and `<br>` line breaks for Medium's importer. Unmarked HTML tables
remain available on the GitHub Pages version; Medium omits imported HTML tables, so the
exporter warns when a table has no immediately preceding curated infographic.

Code blocks retain indentation and internal blank lines. The single terminal newline
added by a Markdown fence is omitted to avoid an unnecessary trailing empty line.
Explicit `<br>` elements are a compatibility measure for importers that collapse
literal newlines; their behaviour in Medium must be verified with a fresh import.
Medium may ignore the language metadata and select CSS or Auto instead. Verify the
language, line breaks, indentation, and absence of extra empty code blocks in the
Medium draft; change the language manually if needed. Re-exporting does not update
an existing Medium draft.

To keep a Markdown table in the source for editing or regenerating its infographic, but
omit it from both generated HTML outputs, wrap it in the export markers:

```markdown
<!-- MEDIUM:EXCLUDE:START -->
| Layer | Owns |
|---|---|
| Bronze | Source fidelity |
<!-- MEDIUM:EXCLUDE:END -->
```

The markers must be paired and ordered `START` then `END`. The exporter fails on malformed
markers rather than risk publishing content that was meant to be excluded.

The exported article starts with a visible `<h1>` title, matching the HTML
`<title>` and `og:title` metadata. The title is extracted from the first Markdown
H1, or the first paragraph for legacy articles without an H1, with leading
article numbering removed. If neither exists, the filename stem is used.
The extracted source title is replaced rather than duplicated. Verify that
Medium imports it as the story title without repeating it in the body.
Previously exported pages need to be re-exported to receive this change.

Article pages embed the following typography in the document head:

```css
body {
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
```

The monospace rule covers both `pre` and `code` because fenced snippets are
exported as plain `<pre>` blocks for importer compatibility. Nested code inherits
the block's font size rather than applying the 0.9 em reduction a second time.

Fonts are not downloaded or embedded. Browsers use the first available font
in each stack, so Charter and Inter require local availability. The styles
apply to the exported website; Medium controls typography after import and
may ignore this CSS. Re-export existing pages to apply the styles.

Article `<img>` attributes are preserved in the exported HTML. The standard
figure reference policy uses `width="1200"` for PNGs below 1600 px wide and
`width="1600"` for PNGs at least 1600 px wide. Pending assets use 1600 provisionally.
Assets below 1200 px are flagged for re-export from their editable or vector source;
do not upscale existing bitmaps. This production threshold is distinct from
Medium's 1192 px threshold for all image placement options.

Retain `style="max-width: 100%; height: auto;"`: images use their preferred
display width when space permits, shrink in narrower containers, and retain
their aspect ratio. The site's 680 px body maximum still limits displayed width.
This does not resize the source PNG. Existing article references are not
automatically migrated; the exporter preserves legacy and custom widths too.
Medium may ignore or replace these attributes during import, so verify image
placement and readability in the Medium draft before publishing.

Every `--site-root` export also creates or updates `index.html` in the publication
repository root. The index contains one titled link per exported article and prevents
GitHub Pages from returning a 404 at the site root.

Commit and push the generated files from `edm_articles_medium`, then configure GitHub
Pages to deploy from the root of its `main` branch. Give the resulting public article
URL to Medium's **Import a story** command. Medium cannot import a local file or localhost
URL.

For this repository pair, the public URL is:

```text
https://georgeschoofs.github.io/edm-articles-medium/Article_01_01/
```

Mermaid fences are exported as code because Medium does not execute Mermaid. Replace
important Mermaid diagrams with PNG or SVG images before importing the story.