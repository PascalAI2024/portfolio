#!/usr/bin/env python3
"""Validate the portfolio's internal evidence graph and optional public URLs."""

from __future__ import annotations

import argparse
import html
import re
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import unquote, urlsplit
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
MARKDOWN_LINK = re.compile(r"!?\x5b[^\x5d]*\x5d\(([^)\n]+)\)")
HTML_LINK = re.compile(r"""(?:href|src)\s*=\s*["']([^"']+)["']""", re.IGNORECASE)
EXTERNAL_SCHEMES = ("http://", "https://")
IGNORED_SCHEMES = ("mailto:", "tel:", "data:", "javascript:")

REQUIRED_README_LINKS = {
    "https://github.com/PascalAI2024/fplbench",
    "https://github.com/PascalAI2024/maple-preview-windows-cuda",
    "https://github.com/PascalAI2024/ZiggyZag",
    "https://github.com/PascalAI2024/JarvisNano",
    "https://ingeniousdigital.com/contact",
    "case-studies/fplbench.md",
    "proof/README.md",
}

INACCESSIBLE_PROOF_URLS = {
    "https://github.com/PascalAI2024/igd-wp",
    "https://github.com/PascalAI2024/VibeFlow",
    "https://mcp.igddev.com/mcp",
    "https://overwatch.igddev.com",
}


def markdown_files() -> list[Path]:
    return sorted(path for path in ROOT.rglob("*.md") if ".git" not in path.parts)


def normalize_target(raw: str) -> str:
    target = html.unescape(raw.strip())
    if target.startswith("<") and ">" in target:
        return target[1 : target.index(">")].strip()
    return target.split(maxsplit=1)[0].strip()


def collect_links(path: Path) -> set[str]:
    text = path.read_text(encoding="utf-8")
    raw_links = MARKDOWN_LINK.findall(text) + HTML_LINK.findall(text)
    return {normalize_target(raw) for raw in raw_links if normalize_target(raw)}


def validate_internal_links(files: list[Path]) -> tuple[list[str], set[str]]:
    errors: list[str] = []
    external: set[str] = set()

    for path in files:
        for target in collect_links(path):
            if target.startswith(EXTERNAL_SCHEMES):
                external.add(target)
                continue
            if target.startswith("#") or target.startswith(IGNORED_SCHEMES):
                continue

            path_part = urlsplit(target).path
            if not path_part:
                continue
            candidate = (path.parent / unquote(path_part)).resolve()
            try:
                candidate.relative_to(ROOT)
            except ValueError:
                errors.append(f"{path.relative_to(ROOT)}: link escapes repository: {target}")
                continue
            if not candidate.exists():
                errors.append(f"{path.relative_to(ROOT)}: missing target: {target}")

    return errors, external


def validate_contract(files: list[Path]) -> list[str]:
    errors: list[str] = []
    readme = (ROOT / "README.md").read_text(encoding="utf-8")

    for required in sorted(REQUIRED_README_LINKS):
        if required not in readme:
            errors.append(f"README.md: required proof or route missing: {required}")

    for path in files:
        text = path.read_text(encoding="utf-8")
        for blocked in sorted(INACCESSIBLE_PROOF_URLS):
            if blocked in text:
                errors.append(
                    f"{path.relative_to(ROOT)}: inaccessible URL cannot be public proof: {blocked}"
                )

    return errors


def check_external_url(url: str) -> tuple[str, str | None]:
    request = Request(
        url,
        headers={
            "User-Agent": "PascalAI-portfolio-link-check/1.0",
            "Accept": "text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8",
        },
    )
    try:
        with urlopen(request, timeout=20) as response:
            if 200 <= response.status < 400:
                return url, None
            return url, f"HTTP {response.status}"
    except HTTPError as exc:
        return url, f"HTTP {exc.code}"
    except (URLError, TimeoutError, OSError) as exc:
        return url, str(exc)


def validate_external_links(urls: set[str]) -> list[str]:
    errors: list[str] = []
    with ThreadPoolExecutor(max_workers=8) as pool:
        futures = {pool.submit(check_external_url, url): url for url in sorted(urls)}
        for future in as_completed(futures):
            url, error = future.result()
            if error:
                errors.append(f"external link failed: {url} ({error})")
    return sorted(errors)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--external",
        action="store_true",
        help="also fetch public HTTP(S) links; intentionally omitted from push CI",
    )
    args = parser.parse_args()

    files = markdown_files()
    internal_errors, external = validate_internal_links(files)
    errors = internal_errors + validate_contract(files)
    if args.external:
        errors.extend(validate_external_links(external))

    if errors:
        print("portfolio validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    suffix = f"; {len(external)} public URLs fetched" if args.external else ""
    print(f"portfolio validation passed: {len(files)} Markdown files{suffix}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
