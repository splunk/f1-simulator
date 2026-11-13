---
title: "Set Up a Board"
linkTitle: "Set Up a Board"
weight: 5
type: "docs"
---

Install the dashboard on a board with the guided installer, then point a rig at it.

{{< callout type="info" >}}
The dashboard code is in the [datadrivers-f1-collector](https://github.com/splunk/datadrivers-f1-collector) repository, which is internal to Splunk. Sign in to GitHub with an account in the Splunk organisation to open it; if the link shows a 404 page, you are not signed in with that account.
{{< /callout >}}

## What you need {#requirements}

- An **ESP32-S3-LCD-1.47B** or **ESP32-C5-LCD-1.47** board and a USB-C data cable.
- A Mac with [Homebrew](https://brew.sh) and Git.
- A Wi-Fi network that the collector can reach. The S3 needs 2.4 GHz; the C5 also supports 5 GHz.

{{% steps %}}

## Install the tools

Run once:

```bash
brew install esptool newt pipx
pipx install 'mpy-cross==1.29.0'
pipx install mpremote
```

## Get the code

```bash
git clone https://github.com/splunk/datadrivers-f1-collector.git
cd datadrivers-f1-collector/esp32-dash
```

## Run the installer

Plug in the board and run:

```bash
tools/flash.sh
```

The installer asks for the board type, its USB port, your Wi-Fi network and password, the UDP port (default `20788`) and the speed units. It then erases the board and installs MicroPython and the dashboard. Press **Ctrl-]** to leave the console it opens at the end.

On the **S3**, the installer asks you to press buttons twice:

1. To enter download mode, hold **BOOT**, press and release **RESET**, then release **BOOT**.
2. After MicroPython is written, press **RESET**.

When it's done, the board shows the Splunk logo, joins Wi-Fi and shows **AWAITING DATA** with its address, for example `192.168.1.50:20788`.

## Connect it to a rig

In the collector, open **Configuration → Rigs** and enter the board's address in **Dash screen** for that rig. Save, then start a race or a playback. See [Optional rig dash screen](/f1-2025/controller-config/#optional-rig-dash-screen).

Give the board a DHCP reservation on your router so its address doesn't change. Use one board per rig.

{{% /steps %}}

## Test without the game {#test}

From the `esp32-dash` folder, send a test lap straight to the board:

```bash
python3 tools/send_test.py --host 192.168.1.50 --port 20788
```

Add `--scenario complete` to show a finished race.

## If it doesn't work {#troubleshooting}

- **Stuck on AWAITING DATA:** check that the rig's **Dash screen** matches the board's address and port exactly, and that the game or a playback is running. The test lap shows whether the board itself works.
- **WIFI FAILED:** check the network name, which is case-sensitive, and the password, then run the installer again.
- **The installer can't read the chip:** put the board in download mode (hold BOOT, press RESET, release BOOT), close any other program using the port, and choose Retry.

The repository's [esp32-dash README](https://github.com/splunk/datadrivers-f1-collector/tree/main/esp32-dash) covers settings, updates and more troubleshooting.
