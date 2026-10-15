# qutebrowser-config

My qutebrowser setup for macOS and Linux.

## Install

```sh
git clone https://github.com/WEBI711/qutebrowser-config.git ~/qutebrowser-config
~/qutebrowser-config/install.sh
```

Then open qutebrowser and run `:adblock-update` once.

## What it does

- JetBrainsMono Nerd Font
- Google as the default search engine and start page
- Google sign-in works (Firefox user agent on `accounts.google.com`)
- WhatsApp Web calls work (Chrome user agent + mic/camera on `web.whatsapp.com`)
- Ad blocker on by default — press `,a` to turn it on or off
- PDF viewer, clipboard paste, downloads to `~/Downloads`

The script links `config.py` and `force-font.css` into place, so `git pull` updates the config.
Run `:config-source` in qutebrowser to reload it.
