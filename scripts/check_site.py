#!/usr/bin/env python3
"""Check Hugo's generated site without third-party dependencies or network access."""

import json
from html.parser import HTMLParser
from pathlib import Path
import sys
from urllib.parse import unquote, urljoin, urlsplit


class Page(HTMLParser):
    def __init__(self, source):
        super().__init__()
        self.ids = set()
        self.references = []
        self.elements = []
        self.h1_count = 0
        self.feed(source)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.elements.append((tag, attrs))
        if attrs.get("id"):
            self.ids.add(attrs["id"])
        if tag == "h1":
            self.h1_count += 1
        for key in ("href", "src"):
            if attrs.get(key):
                self.references.append(attrs[key])


def check(directory):
    root = Path(directory)
    errors = []
    pages = {p.relative_to(root).as_posix(): Page(p.read_text())
             for p in root.rglob("*.html")}
    if "index.html" not in pages:
        raise SystemExit("No homepage found. Run Hugo before checking the site.")
    canonical = next(attrs["href"] for tag, attrs in pages["index.html"].elements
                     if tag == "link" and attrs.get("rel") == "canonical")
    base = urlsplit(canonical)
    prefix = base.path.rstrip("/") + "/"

    expected = {"index.html", "404.html", "f1-2025/index.html", "event_guide/index.html"}
    for section, slugs in {
        "f1-2025": "docker-setup configuration controller-config managing-collectors monitoring pit-wall telemetry dashboards",
        "event_guide": "grand-prix assists rules structure simulation-settings weather go-racing",
    }.items():
        expected.update(f"{section}/{slug}/index.html" for slug in slugs.split())
    if set(pages) != expected:
        errors.append(f"Page set differs: missing={sorted(expected - pages.keys())}; unexpected={sorted(pages.keys() - expected)}")

    def resolve(reference, source_url, label):
        url = urlsplit(urljoin(source_url, reference))
        if url.scheme not in ("http", "https") or url.netloc != base.netloc:
            return None
        if not url.path.startswith(prefix):
            errors.append(f"{label}: link escapes site prefix: {reference}")
            return None
        relative = unquote(url.path[len(prefix):])
        path = root / relative
        if url.path.endswith("/") or path.is_dir():
            path /= "index.html"
        if not path.is_file():
            errors.append(f"{label}: missing target: {reference}")
            return None
        key = path.relative_to(root).as_posix()
        if url.fragment and key in pages and unquote(url.fragment) not in pages[key].ids:
            errors.append(f"{label}: missing anchor: {reference}")
        return key

    references = 0
    for name, page in pages.items():
        source_url = urljoin(canonical, name.removesuffix("index.html"))
        if page.h1_count != 1:
            errors.append(f"{name}: expected one H1, found {page.h1_count}")
        for reference in page.references:
            resolve(reference, source_url, name)
            references += 1
        for tag, attrs in page.elements:
            if tag == "img" and not attrs.get("alt"):
                errors.append(f"{name}: image lacks alternative text: {attrs.get('src')}")
        raw = (root / name).read_text()
        if any(marker in raw for marker in ("!!! warning", "!!! note", "!!! tip", '=== &#34;', "{{<")):
            errors.append(f"{name}: unconverted Markdown or shortcode")

    overview = pages.get("f1-2025/index.html")
    if overview:
        tabs = [attrs for _, attrs in overview.elements if attrs.get("role") == "tab"]
        panels = [attrs for _, attrs in overview.elements if attrs.get("role") == "tabpanel"]
        if len(tabs) != 2 or len(panels) != 2:
            errors.append("Collector overview must render both setup tabs and panels")
        for tab in tabs:
            if tab.get("aria-controls") not in overview.ids:
                errors.append("Setup tab points to a missing panel")

    indexes = list(root.glob("*.search-data.json"))
    if len(indexes) != 1:
        errors.append("Expected one documentation search index")
    else:
        index = json.loads(indexes[0].read_text())
        indexed = set()
        for url, entry in index.items():
            target = resolve(url, canonical, "search")
            if target:
                indexed.add(target)
            if not entry.get("data"):
                errors.append(f"Search entry has no content: {url}")
        if indexed != expected - {"index.html", "404.html"}:
            errors.append("Search must cover exactly the published documentation pages")

    if errors:
        raise SystemExit("Site check failed:\n- " + "\n- ".join(errors))
    print(f"Passed: {len(pages)} HTML pages, {references} links/assets, setup tabs, and {len(indexed)} searchable documentation pages.")


if __name__ == "__main__":
    check(sys.argv[1] if len(sys.argv) > 1 else "public")
