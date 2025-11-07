#!/usr/bin/env bash
set -euo pipefail

# setup_python_env.sh
#
# Idempotent script to ensure a usable Python 3.10 environment and flake8 (alias: norminette)
# Works without sudo. Strategy:
# 1. If a local Python >= 3.10 exists, use it and install flake8 with --user.
# 2. Otherwise install Miniconda into $HOME/miniconda3 and create an env named py310.
# 3. Ensure a 'norminette' shim/script exists at ~/bin/norminette pointing to the flake8 binary.
# 4. Ensure user bin (~/bin) and pip user bin (~/.local/bin) are in shell startup files.

REPO_ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"

MINICONDA_DIR="$HOME/miniconda3"
ENV_NAME="py310"
SHIM_DIR="$HOME/bin"
SHIM_PATH="$SHIM_DIR/norminette"

# Color helpers
BOLD='\033[1m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
RED='\033[0;31m'
CYAN='\033[0;36m'
PASTEL_VIOLET='\033[1;95m'
RESET='\033[0m'

echo "== setup_python_env: starting (repo: ${REPO_ROOT_DIR}) =="

version_ge() {
    # returns 0 if $1 >= $2 (both semantic versions like 3.10.2)
    # usage: version_ge "3.10.2" "3.10"
    [ "$1" = "$2" ] && return 0
    printf '%s\n%s\n' "$1" "$2" | sort -V | tail -n1 | grep -qx "$1"
}

find_python() {
    # try python3.10, then python3, then python
    for p in python3.10 python3 python; do
        if command -v "$p" >/dev/null 2>&1; then
            ver_out="$($p --version 2>&1)"
            # expected output: Python X.Y.Z
            ver="$(printf '%s' "$ver_out" | awk '{print $2}')"
            echo "$p $ver"
            return 0
        fi
    done
    return 1
}

install_miniconda() {
    if [ -d "$MINICONDA_DIR" ]; then
        echo "Miniconda already installed at $MINICONDA_DIR"
        return 0
    fi
        printf "%b\n" "${YELLOW}Installing Miniconda to $MINICONDA_DIR (non-interactive)...${RESET}"
    tmp="$(mktemp -d)"
    installer="$tmp/miniconda.sh"
    curl -fsSL -o "$installer" https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
    bash "$installer" -b -p "$MINICONDA_DIR"
    rm -rf "$tmp"
    echo "Miniconda installed to $MINICONDA_DIR"
    # initialize for zsh/bash shells by appending to rc only if not present
    if ! grep -q "$MINICONDA_DIR/bin" "$HOME/.bashrc" 2>/dev/null; then
        printf "%b\n" "${GREEN}export PATH=\"$MINICONDA_DIR/bin:\$PATH\"${RESET}" >> "$HOME/.bashrc"
    fi
    if [ -f "$HOME/.zshrc" ] && ! grep -q "$MINICONDA_DIR/bin" "$HOME/.zshrc" 2>/dev/null; then
        printf "%b\n" "${GREEN}export PATH=\"$MINICONDA_DIR/bin:\$PATH\"${RESET}" >> "$HOME/.zshrc"
    fi
}

ensure_conda_env() {
    # create env if missing
    if "$MINICONDA_DIR/bin/conda" env list | awk '{print $1}' | grep -qx "$ENV_NAME"; then
        echo "Conda env '$ENV_NAME' already exists"
    else
        printf "%b\n" "${YELLOW}Creating conda env $ENV_NAME with Python 3.10...${RESET}"
        "$MINICONDA_DIR/bin/conda" create -y -n "$ENV_NAME" python=3.10
    fi
}

ensure_shim() {
    mkdir -p "$SHIM_DIR"
    target_flake8="$1"
    if [ -x "$SHIM_PATH" ]; then
        # already exists; check it points to the same flake8
        if grep -Fq "$target_flake8" "$SHIM_PATH" 2>/dev/null; then
            echo "Norminette shim already present and points to $target_flake8"
            return 0
        else
            printf "%b\n" "${YELLOW}Updating existing $SHIM_PATH to point to $target_flake8${RESET}"
        fi
    else
        printf "%b\n" "${YELLOW}Creating norminette shim at $SHIM_PATH -> $target_flake8${RESET}"
    fi
    cat > "$SHIM_PATH" <<EOF
#!/usr/bin/env bash
exec "$target_flake8" "\$@"
EOF
    chmod +x "$SHIM_PATH"
}

ensure_path_in_rc() {
    # arg1 = path to ensure (e.g. $HOME/.local/bin)
    p="$1"
    line="export PATH=\"$p:\$PATH\""
    for rc in "$HOME/.bashrc" "$HOME/.zshrc" "$HOME/.profile"; do
        [ -f "$rc" ] || continue
        if ! grep -Fq "$p" "$rc"; then
            echo "$line" >> "$rc"
            echo "Added $p to PATH in $rc"
        fi
    done
}

main() {
    printf '\n'
    # Quick pre-check: if python3.10 and flake8/norminette are already present
    if command -v python3.10 >/dev/null 2>&1; then
        py_ver_raw="$(python3.10 --version 2>&1 || true)"
        py_ver="$(printf '%s' "$py_ver_raw" | awk '{print $2}')"
        if [[ "$py_ver" == 3.10* ]]; then
            if command -v norminette >/dev/null 2>&1; then
                printf "%b\n" "${GREEN}Found python3.10 -> $py_ver${RESET}"
                printf "%b\n" "${GREEN}Found norminette -> $(command -v norminette)${RESET}"
                norminette --version || true
                printf "%b\n" "${PASTEL_VIOLET}Environment correctly set up: python3.10 and norminette present${RESET}"
                return 0
            elif command -v flake8 >/dev/null 2>&1; then
                printf "%b\n" "${GREEN}Found python3.10 -> $py_ver${RESET}"
                printf "%b\n" "${GREEN}Found flake8 -> $(command -v flake8)${RESET}"
                flake8 --version || true
                printf "%b\n" "${PASTEL_VIOLET}Environment correctly set up: python3.10 and flake8 present${RESET}"
                return 0
            fi
        fi
    fi
    if python_info="$(find_python 2>/dev/null || true)"; then
        set -- $python_info
        py_cmd="$1"
        py_ver="$2"
        printf "%b\n" "${GREEN}Found python: $py_cmd (version $py_ver)${RESET}"
        if version_ge "$py_ver" "3.10"; then
            printf "%b\n" "${GREEN}Using existing Python $py_ver${RESET}"
            # ensure pip and flake8
            if ! "$py_cmd" -m pip --version >/dev/null 2>&1; then
                printf "%b\n" "${YELLOW}pip not present for $py_cmd; attempting ensurepip...${RESET}"
                "$py_cmd" -m ensurepip --upgrade || true
            fi
            printf "%b\n" "${YELLOW}Installing flake8 into user site-packages (no sudo)${RESET}"
            "$py_cmd" -m pip install --user --upgrade pip
            "$py_cmd" -m pip install --user flake8
            flake8_path="$(python3 -m site --user-base 2>/dev/null || true)"
            # try to find flake8 binary path
            if command -v flake8 >/dev/null 2>&1; then
                real_flake8=$(command -v flake8)
            else
                # likely in ~/.local/bin
                if [ -x "$HOME/.local/bin/flake8" ]; then
                    real_flake8="$HOME/.local/bin/flake8"
                else
                    real_flake8=""
                fi
            fi
            if [ -n "$real_flake8" ]; then
                ensure_shim "$real_flake8"
                ensure_path_in_rc "$HOME/.local/bin"
            else
                printf "%b\n" "${RED}Warning: could not locate flake8 binary after install${RESET}"
            fi
        else
            printf "%b\n" "${YELLOW}Found Python $py_ver but < 3.10; will install Miniconda with Python 3.10${RESET}"
            install_miniconda
            ensure_conda_env
            # install flake8 into the env
            env_pip="$MINICONDA_DIR/envs/$ENV_NAME/bin/pip"
            env_flake8="$MINICONDA_DIR/envs/$ENV_NAME/bin/flake8"
            if [ -x "$env_pip" ]; then
                "$env_pip" install --upgrade pip
                "$env_pip" install flake8
                ensure_shim "$env_flake8"
                ensure_path_in_rc "$SHIM_DIR"
            else
                printf "%b\n" "${RED}Unexpected: conda env pip not found at $env_pip${RESET}"
            fi
        fi
    else
        printf "%b\n" "${YELLOW}No usable python found; installing Miniconda and creating Python 3.10 env${RESET}"
        install_miniconda
        ensure_conda_env
        env_pip="$MINICONDA_DIR/envs/$ENV_NAME/bin/pip"
        env_flake8="$MINICONDA_DIR/envs/$ENV_NAME/bin/flake8"
        if [ -x "$env_pip" ]; then
            "$env_pip" install --upgrade pip
            "$env_pip" install flake8
            ensure_shim "$env_flake8"
            ensure_path_in_rc "$SHIM_DIR"
        else
            printf "%b\n" "${RED}Failed: expected pip at $env_pip but not found${RESET}"
            exit 2
        fi
    fi

    printf "%b\n" "\n${BOLD}${CYAN}== Verification ==${RESET}"
    # print python and flake8 versions
    if command -v python3.10 >/dev/null 2>&1; then
        python3.10 --version || true
    fi
    if command -v python3 >/dev/null 2>&1; then
        python3 --version || true
    fi
    if command -v python >/dev/null 2>&1; then
        python --version || true
    fi

    if command -v norminette >/dev/null 2>&1; then
        printf "%b\n" "${GREEN}norminette -> $(command -v norminette)${RESET}"
        norminette --version || true
    elif command -v flake8 >/dev/null 2>&1; then
        printf "%b\n" "${GREEN}flake8 -> $(command -v flake8)${RESET}"
        flake8 --version || true
    else
        printf "%b\n" "${RED}flake8 / norminette not found after installation${RESET}"
        exit 3
    fi

    printf "%b\n" "\n${GREEN}== Done: You may need to open a new terminal to pick up PATH changes. ==${RESET}"
}

main "$@"
