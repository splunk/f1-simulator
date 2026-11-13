---
title: "Collector Configuration"
linkTitle: "Collector Configuration"
weight: 40
type: "docs"
---

Open **Configuration**. The **Event**, **Rigs**, **HEC**, **Observability** and **Queue** tabs share one **Save configuration** button. Settings persist in `/data/config.json`. Use a named Docker volume mounted at `/data` so replacement containers and Watchtower updates reuse them; see [persistent storage](/f1-2025/docker-setup/#verify-persistence).

![v6 Event configuration](../images/v6/config-event.webp)

## General

Under **Event**, set **Event Name** (shown in the collector and Splunk) and **Event ID** (a stable identifier for the event). Keep the ID fixed throughout the event; use a new ID for a new event. **Game** shows **F1 2025**. Leave it on that setting, and set the same UDP format in the game.

Under **Rigs**, add one to four rigs. Give each rig a name and a unique UDP port matching its game settings. Optionally, enter the game machine’s IP address to accept data only from that machine. Standard ports are:

| Rig | UDP port |
| --- | ---: |
| Rig 1 | 20777 |
| Rig 2 | 20778 |
| Rig 3 | 20779 |
| Rig 4 | 20780 |

### Optional rig dash screen

![Rig settings with dash screen and rate controls](../images/v6/config-rigs.webp)

For an ESP32 dash, enter its network address and UDP port in **Dash screen (optional, host:port)** for the corresponding rig, for example `192.168.1.50:20788`. Select a **Dash rate** of 10, 20, 30, 40 or 60 Hz; the default is 10 Hz. The display updates only when new game data arrives, so setting a faster rate cannot make the game send data more frequently. Leave the address blank when no dash is used. To see what the dash shows, see [ESP32 Dashboard](/esp32/). To install it on a board, see [Set Up a Board](/esp32/setup/).

Save changes before assigning drivers. Settings affecting an assigned rig cannot be changed until its race finishes or is reset. Queue and health export settings can be changed during a race.

<span id="what-starting-validates"></span>

## Destinations

Enable HEC, Observability, or both. At least one destination must be configured and enabled before assigning a driver. Blank token fields retain saved tokens. **Test saved connection** uses saved settings, so save first.

### Splunk Enterprise / Cloud

1. Open **HEC** and select **Enable HEC**.
2. Enter the **HEC URL**, such as `https://splunk.example.com:8088`, and token.
3. Save, then select **Test saved connection**.

The HEC token determines the index; the collector has no index override. Use `http://` only for an endpoint actually serving plain HTTP. For HTTPS, certificate verification is enabled by default. The **Allow unverified HEC certificates** option supports self-signed/IP-addressed endpoints when required by your deployment. Observability always verifies certificates.

Changing a destination URL sends its retained backlog to the new address with the original event details. Disabling a destination pauses its backlog; it does not discard it.

### Splunk Observability Cloud

![Observability realm and token configuration](../images/v6/config-observability.webp)

Select **Enable Observability**, choose your organization’s realm and enter its token. Save, then select **Test saved connection**.

The **Metric interval** controls additional sampled measurements sent to Observability; it does not change the rate of every race measurement.

### On Splunk Show

Leave the provisioned HEC settings unchanged unless your administrator directs otherwise. Configure your own Observability realm/token if needed. Confirm the installed release using the footer.

### Automation

Both `POST /update_hec` and `POST /api/update_hec` accept the fields `hec_url`, `hec_token`, and `hec_enabled`. Boolean, 0/1 and quoted equivalents such as `"true"` are accepted. Explicit `null` is rejected. Success returns HTTP 200 with `{"message":"HEC configuration updated successfully"}`.

These routes enable the HEC-only unverified-certificate setting. Existing Ansible requests to port 81 work when that port is published. Apply updates before assigning drivers, and restrict configuration API access to the operator/automation network.

## Queue and health export

The **Queue** tab sets the warning age (default **30 seconds**), disk budget (default **2048 MiB**) and health export (default every **10 seconds**). The warning age never deletes data. At the storage limit, collection reports an error; existing queued batches remain intact.

Health export continues between races. Disable it here if unwanted; the local health view still works. Optional health samples may be skipped to reserve capacity for race data.

## Playback Mode

Use **Recordings → Playback** to replay a saved race on an idle rig, optionally repeated with **Loop**. See [recording and playback instructions](/f1-2025/managing-collectors/#playback).
