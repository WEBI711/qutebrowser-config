# qutebrowser config — shared between macOS and Linux.
# Docs: https://qutebrowser.org/doc/help/settings.html

# Keep settings changed with :set, but this file wins on conflicts.
config.load_autoconfig(True)

# Fonts
c.fonts.default_family = ["JetBrainsMono Nerd Font", "JetBrains Mono", "monospace"]
c.fonts.web.family.fixed = "JetBrains Mono"

# Search: plain text in the address bar searches Google.
c.url.searchengines = {"DEFAULT": "https://www.google.com/search?q={}"}
c.url.start_pages = ["https://www.google.com"]
c.url.default_page = "https://www.google.com"

# Look like regular Chrome, so sites do not block an "unknown" browser.
c.content.headers.user_agent = (
    "Mozilla/5.0 ({os_info}) AppleWebKit/{webkit_version} (KHTML, like Gecko) "
    "{upstream_browser_key}/{upstream_browser_version_short} Safari/{webkit_version}"
)

# Google refuses to sign in from QtWebEngine ("This browser may not be secure").
# A Firefox user agent on the login page alone gets past that check.
config.set(
    "content.headers.user_agent",
    "Mozilla/5.0 ({os_info}; rv:140.0) Gecko/20100101 Firefox/140.0",
    "https://accounts.google.com/*",
)

# Ad blocker. Uses Brave's adblock engine when present, else hosts lists.
# Run :adblock-update once after the first install to fetch the lists.
c.content.blocking.enabled = True
c.content.blocking.method = "auto"
config.bind(",a", "config-cycle --print content.blocking.enabled")

# Everyday-browser comforts
c.content.pdfjs = True
c.content.javascript.clipboard = "access-paste"
c.downloads.location.directory = "~/Downloads"

# Hide finished downloads and bottom-bar messages after 3 seconds.
c.downloads.remove_finished = 3000
c.messages.timeout = 3000

# Show the bottom bar only while typing a command, hinting, etc.
c.statusbar.show = "in-mode"

# Taller, see-through tab bar. window.transparent lets the desktop show
# through; it applies only to windows opened after a restart.
c.window.transparent = True
c.tabs.padding = {"top": 5, "bottom": 5, "left": 8, "right": 8}
c.tabs.indicator.padding = {"top": 3, "bottom": 3, "left": 0, "right": 4}
c.colors.tabs.bar.bg = "rgba(0, 0, 0, 0)"
c.colors.tabs.odd.bg = "rgba(40, 40, 40, 150)"
c.colors.tabs.even.bg = "rgba(40, 40, 40, 150)"
c.colors.tabs.selected.odd.bg = "rgba(90, 90, 90, 200)"
c.colors.tabs.selected.even.bg = "rgba(90, 90, 90, 200)"

# No title bar. Also lets the transparent tab bar show the desktop on macOS.
c.window.hide_decoration = True
