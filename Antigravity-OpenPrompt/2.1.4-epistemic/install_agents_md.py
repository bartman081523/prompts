#!/usr/bin/env python3
"""
install_agents_md.py
Installs the epistemic rules into ~/.gemini/config/AGENTS.md.

Content is taken DIRECTLY and COMPLETELY from the sibling prompt file:
  Antigravity_System_Prompt_2.1.4_epistemic.md

No section filtering, no hardcoded strings — the file is copied verbatim.

Source: gemini-nightly snippets.ts patches 2ec916285, b63ef9210, 54a0fec8e
"""

import shutil
from datetime import datetime
from pathlib import Path

HERE   = Path(__file__).resolve().parent
SOURCE = HERE / "Antigravity_System_Prompt_2.1.4_epistemic.md"
TARGET = Path.home() / ".gemini" / "config" / "AGENTS.md"


def main() -> None:
    if not SOURCE.exists():
        raise FileNotFoundError(f"Source prompt not found: {SOURCE}")

    content = SOURCE.read_text(encoding="utf-8")

    TARGET.parent.mkdir(parents=True, exist_ok=True)

    if TARGET.exists():
        backup = TARGET.with_suffix(
            f".bak.{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
        )
        shutil.copy2(TARGET, backup)
        print(f"Backed up existing AGENTS.md → {backup}")

    TARGET.write_text(content, encoding="utf-8")
    lines = content.count("\n")
    print(f"✓ Written {lines} lines to {TARGET}")
    print(f"  Source: {SOURCE}")


if __name__ == "__main__":
    main()
