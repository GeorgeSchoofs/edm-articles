---
name: article-medium-export
description: "Export one or more article drafts as Medium-importable HTML and refresh the publication site index. Use when asked to export articles for Medium, create Medium-ready pages, or refresh the static article publication site."
argument-hint: "Article filenames or paths, for example Article_00_01 and Article_01_01"
---

# Medium Article Export

Export article Markdown using the repository's `tools/medium_export.py` script.
The script is the source of truth for conversion behavior; do not recreate its
Markdown or HTML transformations in this workflow.

## Scope

- Accept one or more article filenames or paths. Filenames such as
  `Article_01_02` resolve to `series1/Article_01_02.md`.
- Use the sibling publication repository `../edm_articles_medium` as the site
  root and `https://georgeschoofs.github.io/edm-articles-medium/<ArticleStem>/`
  as each article's public base URL.
- Export HTML and assets only. Do not commit, push, or deploy unless the user
  explicitly requests those actions.

## Workflow

1. Confirm each requested source Markdown file exists in `series1/`.
2. Confirm the exporter dependencies are available. If imports fail, direct the
   user to install `requirements-medium.txt` with `python -m pip install -r
   requirements-medium.txt`; do not install packages without need.
3. Run the exporter sequentially for each requested article. Sequential runs
   avoid concurrent writes to the shared publication index:

   ```powershell
   python tools/medium_export.py series1/Article_01_02.md `
     --site-root ..\edm_articles_medium `
     --base-url https://georgeschoofs.github.io/edm-articles-medium/Article_01_02/
   ```

   Substitute each requested article stem in both the source path and URL.
4. Treat a non-zero exit as an export failure and report the command output. The
   exporter fails when a referenced local image does not exist; do not create
   placeholder images or silently remove the reference.
5. Verify that each requested article has
   `../edm_articles_medium/<ArticleStem>/index.html`, that its referenced local
   images were copied to that article's `images/` directory, and that the root
   `index.html` contains each requested article link.
6. Report output paths and warnings. The exporter warns about HTML tables that
   Medium will omit when no infographic image immediately precedes them. Report
   these warnings; do not alter article content or invent replacement graphics
   as part of export. Apply the image checks below and distinguish manual
   observations from warnings emitted by the exporter.

## Image sizing checks

- Preserve source image dimensions during export. Do not resample, upscale, crop,
  or regenerate assets as part of this skill.
- Preserve figure display attributes in the exported HTML. The standard article
  markup uses `width="700"` and `style="max-width: 100%; height: auto;"` to provide
  a responsive website display size without changing the image file's resolution.
  Verify that these attributes survive export when present in the source.
  Medium may ignore or replace them on import; they do not guarantee its layout.
- Inspect the pixel dimensions of referenced local infographic assets. The
  designer/Claude production default is 1600 px wide with proportional height;
  it is not a mandatory size for existing assets or Napkin exports.
- Napkin's 1x, 2x, and 3x resolution settings are selected manually during image
  export. Check the resulting dimensions rather than assuming a multiplier
  produces a particular width. Do not impose designer pixel-size instructions
  on Napkin briefs.
- Medium's [image guidance](https://help.medium.com/hc/en-us/articles/215679797-Using-images)
  states that images must be at least 1192 px wide for all placement options to
  appear. Report narrower images as a placement limitation, not an export failure.
- When visual inspection is available, check infographic readability at
  approximately 700 px and 350 px displayed width. These are design test widths,
  not fixed Medium dimensions. Report tiny labels or overly dense layouts;
  increasing resolution alone will not fix them. If not inspected, explicitly
  report readability as unverified.
- Medium controls its own image layout. The static publication site's native
  image size is not evidence of how Medium will display the imported story.
  Confirm placement, captions, alt text, and desktop/mobile readability in the
  Medium draft before publishing; HTML export alone does not verify them.

## Export behavior and limitations

- The exporter removes the internal review block and the intended-audience line.
- Fenced code is converted to plain `<pre>` markup with language metadata.
- Local article images are copied and rewritten to public absolute URLs when a
  base URL is supplied.
- HTML tables remain in the generated GitHub Pages HTML, but Medium's importer
  omits them. A warning identifies tables without a preceding curated visual.
- Mermaid fences are exported as code because Medium does not render Mermaid.
  Important diagrams need an exported image before Medium import.
- The site root index is updated on every `--site-root` run while preserving its
  existing article links.

## Out of scope

- Proofreading, editorial approval, or changing article prose.
- Creating or editing infographic assets.
- Git commits, pushes, or GitHub Pages deployment unless requested.