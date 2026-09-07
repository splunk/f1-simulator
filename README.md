# Splunk Data Drivers documentation

The F1 2025 documentation site, built with Hugo and the pinned Hextra theme.

## Preview locally

Install Hugo **0.165.0** and Go **1.23 or newer**, then run:

```sh
hugo server --disableFastRender
```

Open the URL Hugo prints (normally `http://localhost:1313/f1-simulator/`).
The first build downloads Hextra and its search/image-zoom libraries. Later
builds reuse Hugo's cache. Node.js and Python packages are not needed.

## Build and check

```sh
hugo --gc --minify --panicOnWarning
python3 scripts/check_site.py public
```

The check uses Python 3's standard library. It verifies the published page set,
internal links and anchors, images, styles/scripts, search coverage, and conversion
of tabs and callouts. Generated output in `public/` is ignored by Git.

## Editing documentation

- `content/_index.md`: homepage metadata.
- `content/f1-2025/`: collector documentation. `_index.md` is the overview.
- `content/event_guide/`: the seven F1 2025 event setup pages and guide index.
- `static/assets/`: screenshots and car artwork copied unchanged to the site.
- `static/favicon.ico`: the site favicon, published at `/favicon.ico` under the base URL.
- `layouts/home.html`: the orange landing page and documentation shortcuts.
- `assets/`: CSS, JavaScript and search data processed by Hugo's asset pipeline.
- `assets/css/custom.css`: branding and responsive layout overrides.
- `hugo.yaml`: navigation and theme settings.

Page titles and sidebar order come from `title`, `linkTitle` and `weight` in
YAML front matter. Use Hugo content paths for internal links, for example
`[Configuration](/f1-2025/controller-config/#general)`; the theme adds the
GitHub Pages prefix. Image paths start with `/assets/`.

Use Hextra shortcodes for callouts and tabs:

```markdown
{{< callout type="warning" >}}
**Deploying stops collection**

Turn Master Control back on after deploying configuration.
{{< /callout >}}

{{< tabs >}}
{{< tab name="Splunk Show" >}}
Instructions for an existing Show instance.
{{< /tab >}}
{{< tab name="Run locally" >}}
Instructions for Docker.
{{< /tab >}}
{{< /tabs >}}
```

The site uses Hugo's default project directories without custom content or
static mounts. New pages under `content/` and files under `static/` are included
automatically. Keep only F1 2025 and the current event guide in these directories.
When adding a page, update the expected page list in `scripts/check_site.py`.

The remaining `archive/mkdocs/` files are retired MkDocs material, excluded from the build
and search. The imported theme's mounts omit its demo static files so only our
own images and favicon are published. The previous MkDocs configuration has
been retired.

## Hextra content components

- Use `{{% steps %}}` around a setup procedure, with a heading for each stage.
  Keep existing heading names when editing to preserve incoming anchor links.
- Use `cards` and `card` for navigation groups. On section overview pages, links
  such as `link="./telemetry/"` keep the GitHub Pages prefix intact.
- Use `{{< details title="Explanation" closed="true" >}}` for optional supporting
  material. Keep warnings and required actions outside collapsed panels.
- Use `{{< term "HEC" >}}`, `{{< term "UDP" >}}` or `{{< term "realm" >}}` for
  the first relevant mention on a page. Definitions are in `data/en/termbase.yaml`.
  They appear on hover or keyboard focus and can be dismissed with Escape.

Goldmark HTML rendering is enabled for Hextra's Steps and nested shortcodes.
Content is authored and reviewed in this repository; do not import untrusted HTML.

## GitHub Pages

`.github/workflows/docs.yml` builds and validates pull requests. Pushes to `main`
also deploy the validated `public/` artifact to GitHub Pages.

For the initial migration, set **Settings → Pages → Build and deployment →
Source** to **GitHub Actions**. This replaces the former branch-based MkDocs
deployment when the workflow first runs. The configured public URL is
`https://splunk.github.io/f1-simulator/`; existing F1 2025 and event-page URLs
are retained. Change `baseURL` in `hugo.yaml` if deploying somewhere else.

The theme is pinned in `go.mod` and `go.sum`. When updating Hugo or Hextra,
re-run the build and site check and review the homepage, documentation navigation,
tabs, search and mobile layout. Local theme overrides cover the branded homepage,
dark page shell, fixed dark preference, favicon, 404 page and documentation-only
search data. The small icon helper uses Hugo's current `hugo.Data` API.
