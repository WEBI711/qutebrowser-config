#!/usr/bin/env bash
# Install qutebrowser + JetBrainsMono Nerd Font, link config files, and make qutebrowser the default browser.
set -euo pipefail

REPO_DIR="$(cd "$(dirname "$0")" && pwd)"

main() {
  install_packages
  link_config config.py
  link_config force-font.css
  set_default_browser
  echo
  echo "Done. Open qutebrowser and run :adblock-update once to fetch the ad block lists."
}

# Helpers

install_packages() {
  case "$(uname -s)" in
    Darwin)
      brew install --cask qutebrowser font-jetbrains-mono-nerd-font
      ;;
    Linux)
      if command -v pacman >/dev/null; then
        sudo pacman -S --needed qutebrowser python-adblock ttf-jetbrains-mono-nerd
      elif command -v apt-get >/dev/null; then
        sudo apt-get install -y qutebrowser fonts-jetbrains-mono
      elif command -v dnf >/dev/null; then
        sudo dnf install -y qutebrowser jetbrains-mono-fonts-all
      else
        echo "Unknown package manager. Install qutebrowser and JetBrains Mono by hand."
      fi
      ;;
  esac
}

link_config() {
  local file="$1"
  local config_dir
  config_dir="$(qutebrowser_config_dir)"
  mkdir -p "$config_dir"

  local target="$config_dir/$file"
  if [ -e "$target" ] && [ ! -L "$target" ]; then
    mv "$target" "$target.backup"
    echo "Backed up old $file to $target.backup"
  fi
  ln -sfn "$REPO_DIR/$file" "$target"
  echo "Linked $target -> $REPO_DIR/$file"
}

qutebrowser_config_dir() {
  if [ "$(uname -s)" = "Darwin" ]; then
    echo "$HOME/.qutebrowser"
  else
    echo "${XDG_CONFIG_HOME:-$HOME/.config}/qutebrowser"
  fi
}

set_default_browser() {
  if [ "$(uname -s)" = "Darwin" ]; then
    echo "macOS: set the default browser in System Settings > Desktop & Dock > Default web browser."
  elif command -v xdg-settings >/dev/null; then
    xdg-settings set default-web-browser org.qutebrowser.qutebrowser.desktop
    echo "Set qutebrowser as the default browser."
  fi
}

main "$@"
