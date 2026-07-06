#!/usr/bin/env bash
# install_agents_md.sh
# Installs the epistemic rules into ~/.gemini/config/AGENTS.md.
# Content is taken DIRECTLY and COMPLETELY from the sibling prompt file:
#   Antigravity_System_Prompt_2.1.4_epistemic.md
# Safe to re-run: backs up any existing file before overwriting.

set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SOURCE="$HERE/Antigravity_System_Prompt_2.1.4_epistemic.md"
TARGET="$HOME/.gemini/config/AGENTS.md"
BACKUP="${TARGET}.bak.$(date +%Y%m%d_%H%M%S)"

if [[ ! -f "$SOURCE" ]]; then
  echo "Error: Source prompt not found at $SOURCE" >&2
  exit 1
fi

TARGET_DIR="$(dirname "$TARGET")"
mkdir -p "$TARGET_DIR"

if [[ -f "$TARGET" ]]; then
  echo "Backing up existing AGENTS.md → $BACKUP"
  cp "$TARGET" "$BACKUP"
fi

cp "$SOURCE" "$TARGET"
echo "✓ Written $(wc -l < "$TARGET") lines to $TARGET"
echo "  Source: $SOURCE"
