# qutebrowser-config

My qutebrowser setup for macOS and Linux.

## Install

```sh
git clone https://github.com/WEBI711/qutebrowser-config.git ~/qutebrowser-config
~/qutebrowser-config/install.sh
```

Then open qutebrowser and run `:adblock-update` once.

## What it does

- JetBrains Mono font
- Google as the default search engine and start page
- Google sign-in works (Firefox user agent on `accounts.google.com`)
- Ad blocker on by default — press `,a` to turn it on or off
- PDF viewer, clipboard paste, downloads to `~/Downloads`

The script links `config.py` into place, so `git pull` updates the config.
Run `:config-source` in qutebrowser to reload it.
