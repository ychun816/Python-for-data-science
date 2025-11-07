#!/usr/bin/env bash
set -eu

# cleanup_python00_pycache.sh
# Remove __pycache__ directories and .pyc files under Python00

ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"

echo "Searching for Python repos under: $ROOT_DIR"

shopt -s nullglob
for repo in "$ROOT_DIR"/Python*; do
    [ -d "$repo" ] || continue
    echo
    echo "Cleaning repo: $(basename "$repo")"
    find "$repo" -type d -name "__pycache__" -print -exec rm -rf {} + || true
    find "$repo" -type f -name "*.pyc" -print -delete || true
done

# Print a bold baby-blue confirmation (ANSI escape). "Baby blue" mapped to bright cyan.
BOLD='\033[1m'
BABY_BLUE='\033[1;96m'
RESET='\033[0m'
printf "%b\n" "${BOLD}${BABY_BLUE}CLEANUP DONE!! ໒(⊙ᴗ⊙)७✎${RESET}"
