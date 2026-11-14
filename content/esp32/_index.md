---
title: "ESP32 Dashboard"
linkTitle: "ESP32 Dashboard"
weight: 30
type: "docs"
sidebar: {"open": true}
cascade: {"type": "docs"}
---

The ESP32 dashboard is a small race dash that sits on the rig and shows the driver's live data from the collector. It is optional: the collector, the dashboards and the event run the same without it.

![The race dash on the board's screen](images/hud.webp)

To install it on a board, see [Set Up a Board](/esp32/setup/).

## Supported boards

The dashboard runs MicroPython on three small colour-screen boards:

- **Waveshare ESP32-S3-LCD-1.47B**, which also turns the picture the right way up when the board is turned over.
- **Waveshare ESP32-C5-LCD-1.47**
- **LilyGo T-Display-S3**, the 1.9-inch version without touch.

Each board's **BOOT** button switches between the race dash and the lap timing view; on the T-Display-S3 its other button does the same. The Waveshare boards also have an RGB LED that repeats the most important colour on the screen. The T-Display-S3 has no LED.

## How the collector sends to it

Each rig can send to one dash. In the collector, set the rig's **Dash screen** to the address the board shows while it waits for data, for example `192.168.1.50:20788`, and choose a **Dash rate** (10 Hz by default). See [Optional rig dash screen](/f1-2025/controller-config/#optional-rig-dash-screen).

The collector sends one small UDP packet per update to that address while the rig is racing, and keeps sending the result once the race ends. The board doesn't reply, so a dash that is switched off or out of range does not affect the collector. The collector must be able to reach the board over the network; a DHCP reservation keeps the board's address the same.

## In this section

{{< cards cols="3" >}}
{{< card link="./setup/" title="Set up a board" subtitle="Install the dashboard and connect it to a rig." >}}
{{< card link="./screens/" title="Screens and LED" subtitle="The race dash, lap timing and race result screens." >}}
{{< card link="./browser/" title="Browser view" subtitle="Watch the dash from a phone or laptop." >}}
{{< /cards >}}
