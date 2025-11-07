#!/usr/bin/env bash
set -eu

# Run all exercises in Python00/ex00..ex09 by executing any .py file that
# contains the "if __name__ == '__main__'" guard. Prints a header for each
# file and continues on errors.

ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"

echo "Searching for Python repos under: $ROOT_DIR"

shopt -s nullglob

# Color helpers
BOLD='\033[1m'
BABY_BLUE='\033[1;96m'
CYAN='\033[1;36m'
GREEN='\033[0;32m'
RED='\033[0;31m'
RESET='\033[0m'

# Explicit list of repos. Comment out lines for repos you don't want to run.
REPOS=(
    "Python00"
    # "Python01"
    # "Python02"
    # "Python03"
    # "Python04"
)

for repo_name in "${REPOS[@]}"; do
    repo="$ROOT_DIR/$repo_name"
    [ -d "$repo" ] || continue
    echo
    printf "%b\n" "${BOLD}${BABY_BLUE}================================================================${RESET}"
    printf "%b\n" "${BOLD}${CYAN}Repo: $repo_name${RESET}"
    printf "%b\n" "${BOLD}${BABY_BLUE}================================================================${RESET}"
    for ex in "$repo"/ex{00..09}; do
        [ -d "$ex" ] || continue
        echo
        printf "%b\n" "${BOLD}${BABY_BLUE}================================================================${RESET}"
        printf "%b\n" "${BOLD}${CYAN}Exercise: $(basename "$ex")${RESET}"
        printf "%b\n" "${BOLD}${BABY_BLUE}----------------------------------------------------------------${RESET}"
    ran=false
    for py in "$ex"/*.py; do
        # Only run files that contain a main guard to avoid importing modules
        if grep -q "__name__ *== *['\"]__main__['\"]" "$py"; then
                echo
                printf "%b\n" "${GREEN}--- Running: $py ---${RESET}"
            # run in a subshell so it doesn't affect this script's environment
            (
                cd "$ex"
                # use python3 where available
                if command -v python3 >/dev/null 2>&1; then
                    python3 "$(basename "$py")"
                else
                    python "$(basename "$py")"
                fi
            ) || echo "[error] script $py exited with code $?"
            ran=true
        fi
    done
    if [ "$ran" = false ]; then
            printf "%b\n" "${RED}No runnable scripts with a main guard found in $(basename "$ex")${RESET}"
    fi
done

done

    echo
    # echo "ALL DONE! ᕕ(⌐■_■)ᕗ ♪♬"
    BOLD='\033[1m'
    BABY_BLUE='\033[1;96m'
    RESET='\033[0m'
    printf "%b\n" "${BOLD}${BABY_BLUE}ALL DONE! ᕕ(⌐■_■)ᕗ ♪♬${RESET}"
