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

The command writes `../edm_articles_medium/Article_01_01/index.html`. It removes the internal
review block and audience line, copies local images, and converts fenced code to plain
`<pre>` markup with explicit language metadata for Medium's importer. HTML tables remain
available on the GitHub Pages version. Because Medium omits imported HTML tables, the
exporter warns when a table has no immediately preceding curated infographic.

Article `<img>` attributes are preserved in the exported HTML. The standard
figure markup uses `width="700"` and `style="max-width: 100%; height: auto;"`:
images display at 700 CSS pixels when space permits, shrink in narrower
containers, and retain their aspect ratio. This does not resize the source PNG.
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