---
title: "Browser View"
linkTitle: "Browser View"
weight: 20
type: "docs"
---

The board also serves its dash as a web page, so a phone, tablet or laptop on the same network can show exactly what the board shows. Open `http://<board IP>/`, using the address from the AWAITING DATA screen without the port, for example `http://192.168.1.50/`.

![The dash in a browser, race dash in Sharp mode](../images/browser-hud-sharp.webp)

The dot under the dash is the board's LED.

## Controls {#controls}

- **HUD / Lap** switches the view in that browser only. It doesn't change the board, and the board's BOOT button doesn't change the browser.
- **Pixel** shows the screen's own pixels, scaled up. **Sharp** draws the same screen at the browser's resolution.
- Each browser remembers its choices.

![The dash in a browser, lap timing view in Pixel mode](../images/browser-lap-pixel.webp)

## Good to know {#notes}

- Up to three browsers can watch at once. Another one shows **Disconnected**.
- A browser that opens the page during a race starts from what the board is showing.
- The page is read-only plain HTTP with no login. Nothing on it changes the board or the collector.

To turn the page off, see [The dash in a browser](https://github.com/splunk/datadrivers-f1-collector/tree/main/esp32-dash#the-dash-in-a-browser) in the esp32-dash guide.
