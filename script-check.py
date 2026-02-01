#!/usr/bin/env python3
import re
import sys
from pathlib import Path

try:
    import yaml  # pip install pyyaml
except ImportError:
    print("ERROR: Missing dependency pyyaml. Install with: pip install pyyaml", file=sys.stderr)
    sys.exit(2)

def fail(msg: str) -> None:
    print(f"ERROR: {msg}", file=sys.stderr)
    sys.exit(1)

# Match headings like:
# "## E.1 – Glossary" or "# G.2 - Current Situation"
MAJOR_HEADING_RE = re.compile(r"^#{1,6}\s+([EGPS]\.\d+)\b", re.MULTILINE)

def main() -> None:
    manifest_path = Path("fichier-test.yml")
    if not manifest_path.exists():
        fail(f"Manifest not found: {manifest_path}")

    manifest = yaml.safe_load(manifest_path.read_text(encoding="utf-8"))
    file_path = Path(manifest.get("file", ""))
    required = manifest.get("required", [])

    if not file_path:
        fail("fichier-test.yml must contain 'file:'")
    if not required:
        fail("fichier-test.yml must contain a non-empty 'required:' list")
    if not file_path.exists():
        fail(f"Spec file not found: {file_path}")

    text = file_path.read_text(encoding="utf-8", errors="replace")

    found = set(m.group(1) for m in MAJOR_HEADING_RE.finditer(text))
    missing = [sec for sec in required if sec not in found]

    if missing:
        fail(f"Missing major section(s) in {file_path}: {missing}")

    print(f"OK: All required major sections are present in {file_path}")

if __name__ == "__main__":
    main()
