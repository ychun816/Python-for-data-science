#!/usr/bin/env bash
set -eu

# PUT IN REPO WITH EX FOLDERS TO RUN THEM!! 
# Run all exercises in Python00/ex00..ex09 by executing any .py file that
# contains the "if __name__ == '__main__'" guard. Prints a header for each
# file and continues on errors.

ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"

echo "Searching for Python repos under: $ROOT_DIR"

shopt -s nullglob

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

# Test argument for ex05 (single-line, newlines collapsed to spaces)
TEST_ARG="Python 3.0, released in 2008, was a major revision that is not completely backward-compatible with earlier versions. Python 2 was discontinued with version 2.7.18 in 2020."

# Explicit list of repos. Comment out lines for repos you don't want to run.
REPOS=(
    # If your exercises are directly in this repo (ex00..ex09) keep "." here
    "."
    "Python00"
    "Python01"
    "Python02"
    "Python03"
    "Python04"
)


for repo_name in "${REPOS[@]}"; do
    repo="$ROOT_DIR/$repo_name"
    [ -d "$repo" ] || continue
    echo
    # Repo header: show a bold orange message about running flake8
    # printf "%b\n" "${BOLD}${BABY_BLUE}================================================================${RESET}"
    printf "%b\n" "${BOLD}${BG_PASTEL_ORANGE}${FG_BLACK} Repo: $(basename "$repo") ${RESET}"

    # Run flake8 linting for this repo (if available)
    # printf "%b\n" "${BOLD}${FG_ORANGE}run flake8 (will show errors below if found): $repo_name${RESET}"
    # flake8 "$repo" #|| true
    if command -v flake8 >/dev/null 2>&1; then
        printf "%b\n" "${FG_ORANGE}Running flake8 for $(basename "$repo")...${RESET}"
        # run flake8 and show results; do not stop on lint failures
        if ! flake8 "$repo"; then
            printf "%b\n" "${BOLD}${RED}flake8 reported issues in $(basename "$repo") (see above)${RESET}"
        else
            printf "%b\n" "${BOLD}${FG_ORANGE}flake8 passed for $(basename "$repo")${RESET}"
        fi
    else
        printf "%b\n" "${BOLD}${RED}flake8 not found, skipping lint for $(basename "$repo")${RESET}"
    fi

    # printf "%b\n" "${BOLD}${BABY_BLUE}================================================================${RESET}"
    for ex in "$repo"/ex{00..09}; do
        [ -d "$ex" ] || continue
        echo
        printf "%b\n" "${BOLD}${BABY_BLUE}================================================================${RESET}"
        printf "%b\n" "${BOLD}${CYAN}Exercise: $(basename "$ex")${RESET}"
        printf "%b\n" "${BOLD}${BABY_BLUE}----------------------------------------------------------------${RESET}"
    ran=false
            for py in "$ex"/*.py; do
                # Run files that contain a main guard, or runner/test files named
                # `tester.py` (some exercises use a tester script without a guard).
                if grep -q "__name__ *== *['\"]__main__['\"]" "$py" || [ "$(basename "$py")" = "tester.py" ]; then
                echo
                printf "%b\n" "${GREEN}--- Running: $py ---${RESET}"
            # run in a subshell so it doesn't affect this script's environment
            (
                cd "$ex"
                # use python3 where available
                if command -v python3 >/dev/null 2>&1; then
                    if [ "$(basename "$ex")" = "ex05" ]; then
                        # pass the long test argument to ex05
                        python3 "$(basename "$py")" "$TEST_ARG"
                    else
                        python3 "$(basename "$py")"
                    fi
                else
                    if [ "$(basename "$ex")" = "ex05" ]; then
                        python "$(basename "$py")" "$TEST_ARG"
                    else
                        python "$(basename "$py")"
                    fi
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
    printf "%b\n" "${BOLD}${PASTEL_VIOLET}ALL DONE! ᕕ(⌐■_■)ᕗ ♪♬${RESET}"
