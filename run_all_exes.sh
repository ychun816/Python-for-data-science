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
    # "Python00"
    # "Python01"
    "Python02"
    # "Python03"
    # "Python04"
)


for repo_name in "${REPOS[@]}"; do
    repo="$ROOT_DIR/$repo_name"
    [ -d "$repo" ] || continue
    echo
    # Repo header: show a bold orange message about running flake8
    # printf "%b\n" "${BOLD}${BABY_BLUE}================================================================${RESET}"
    printf "%b\n" "${BOLD}${BG_PASTEL_ORANGE}${FG_BLACK} Repo: $repo_name ${RESET}"

    # Run flake8 linting for this repo (if available)
    # printf "%b\n" "${BOLD}${FG_ORANGE}run flake8 (will show errors below if found): $repo_name${RESET}"
    # flake8 "$repo" #|| true
    if command -v flake8 >/dev/null 2>&1; then
        printf "%b\n" "${FG_ORANGE}Running flake8 for $repo_name...${RESET}"
        # run flake8 and show results; do not stop on lint failures
        if ! flake8 "$repo"; then
            printf "%b\n" "${BOLD}${RED}flake8 reported issues in $repo_name (see above)${RESET}"
        else
            printf "%b\n" "${BOLD}${FG_ORANGE}flake8 passed for $repo_name${RESET}"
        fi
    else
        printf "%b\n" "${BOLD}${RED}flake8 not found, skipping lint for $repo_name${RESET}"
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
                # Default: run from the exercise directory so relative imports/paths work
                run_cwd="$ex"
                run_cmd=( )

                exbase=$(basename "$ex")
                pybase=$(basename "$py")

                # Special-case ex00 tester: data lives in "$repo/data" so run the
                # tester from that directory (tester.py expects the CSV in cwd).
                if [ "$exbase" = "ex00" ] && [ "$pybase" = "tester.py" ]; then
                    run_cwd="$repo/data"
                    # execute the tester by its relative path from data directory
                    run_cmd=(python3 "$repo/$exbase/$pybase")

                # ex01 expects a single country argument
                elif [ "$exbase" = "ex01" ]; then
                    # Ensure the expected CSV exists next to aff_life.py by creating
                    # a temporary symlink into the exercise directory pointing to
                    # the repo data file. We remove it after running.
                    link="$repo/$exbase/life_expectancy_years.csv"
                    target="$repo/data/life_expectancy_years.csv"
                    if [ ! -f "$link" ] && [ -f "$target" ]; then
                        ln -s "$target" "$link" || true
                        cleanup_link=true
                    else
                        cleanup_link=false
                    fi
                    run_cmd=(python3 "$pybase" "France")

                # ex02 expects two country args
                elif [ "$exbase" = "ex02" ]; then
                    # ex02 requires population_total.csv under repo/data. If the
                    # CSV is missing or broken, skip this exercise to avoid
                    # spurious failures in the batch runner.
                    poppath="$repo/data/population_total.csv"
                    if [ ! -f "$poppath" ]; then
                        echo "[skip] population_total.csv not found; skipping ex02"
                        exit 0
                    fi
                    run_cmd=(python3 "$pybase" "France" "Germany")

                # ex03 expects a year argument; pass --save so headless runs succeed
                elif [ "$exbase" = "ex03" ]; then
                    out="$repo/${exbase}_2019_cli.png"
                    run_cmd=(python3 "$pybase" "2019" "--save" "$out")

                # ex05 still needs the long TEST_ARG
                elif [ "$exbase" = "ex05" ]; then
                    run_cmd=(python3 "$pybase" "$TEST_ARG")

                else
                    # generic runner: use python3 without extra args
                    run_cmd=(python3 "$pybase")
                fi

                # If python3 is unavailable, fall back to python
                if ! command -v python3 >/dev/null 2>&1; then
                    # replace command with python where necessary
                    if [ "${run_cmd[0]}" = "python3" ]; then
                        run_cmd=(python "${run_cmd[@]:1}")
                    fi
                fi

                # Run the prepared command from the chosen working directory
                cd "$run_cwd"
                "${run_cmd[@]}"

                # Cleanup any temporary symlink created for ex01
                if [ "${cleanup_link:-false}" = true ]; then
                    rm -f "$repo/$exbase/life_expectancy_years.csv" || true
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
