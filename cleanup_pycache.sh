#!/usr/bin/env bash
set -eu

# Color helpers
BOLD='\033[1m'
BABY_BLUE='\033[1;96m'
PASTEL_VIOLET='\033[1;95m'
CYAN='\033[1;36m'
GREEN='\033[0;32m'
RED='\033[0;31m'
RESET='\033[0m'

# Pastel orange background (256-color) with black foreground for contrast
BG_PASTEL_ORANGE='\033[48;5;215m'
FG_BLACK='\033[30m'
FG_ORANGE='\033[38;5;208m'


# cleanup_python00_pycache.sh
# Remove __pycache__ directories and .pyc files under Python00

ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"

echo "Searching for Python repos under: $ROOT_DIR"

shopt -s nullglob
for repo in "$ROOT_DIR"/Python*; do
    [ -d "$repo" ] || continue
    echo
    printf "${BOLD}${BG_PASTEL_ORANGE}Cleaning repo: $(basename "$repo")${RESET}"
    printf "\n"
    find "$repo" -type d -name "__pycache__" -print -exec rm -rf {} + || true
    find "$repo" -type f -name "*.pyc" -print -delete || true
done

# Print a bold pastel violet confirmation (ANSI escape).
printf "%b\n" "${BOLD}${PASTEL_VIOLET}\nCLEANUP DONE!! ໒(⊙ᴗ⊙)७✎ ${RESET}"
