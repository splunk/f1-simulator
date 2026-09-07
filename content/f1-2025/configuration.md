---
title: "Using the Collector"
linkTitle: "The Collector Page"
weight: 30
type: "docs"
---

The **Collector** page at `/` is the operator screen. Everything needed to run an event is on it: the master switch, one card per rig, and the Logs, Health, and Config panels.

![The Collector page during a session](/assets/screenshots/f1-2025/collector.png)

## Status bar

| Control | Meaning |
| --- | --- |
| **Master Control** | The master switch. **SYSTEMS LIVE** means the UDP listeners and delivery workers are running; **SYSTEMS OFFLINE** means nothing is being collected. |
| **PLAYBACK MODE** | An amber badge shown when the collector is replaying a recorded `.tlm` file instead of listening for live UDP. |
| Public address | The collector's public IP address, shown with a blue indicator. This is the address to enter in F1 25 for an internet-reachable collector. |
| **Runtime State** | Green when the collector's shared runtime state is available. Red means the UI cannot read live values. |
| **MEM** | Total memory used by the single collector process for all rigs — not memory per rig. |
| **n/n Collectors** | How many of the configured rigs currently have a running collector. |

The **Logs**, **Health**, and **Config** buttons on the right open the three operator panels.

{{< callout type="info" >}}

**The address badge is the public IP only**

The badge shows an address, not a port. Each rig's UDP port is on its own card. On a LAN-only deployment, use the Docker host's LAN address rather than the public one.

{{< /callout >}}

## Rig cards

Each enabled rig has its own card. The card border and state line are colour-coded:

| State line | Meaning |
| --- | --- |
| **Telemetry live** | The collector is running and receiving UDP packets. |
| **Telemetry playback** | The collector is running and replaying a recorded file. |
| **Awaiting telemetry** | The collector is running but no packets have arrived recently. |
| **Awaiting playback** | Playback is configured but has not produced packets yet. |
| **Race complete** | Final Classification was received for this session. |
| **Collector stopped** | Master Control is off, or this rig failed to start. |

The pills along the top of each card show:

- **RIG n** — the rig identifier used in the delivered data
- **UDP nnnnn** — the rig's UDP port; green when packets arrived recently
- **REC** — this rig is currently writing a `.tlm` recording
- **REC ERROR** — this rig could not create or write its recording file; hover for the error
- **O11y ✓ / ✗ / —** and **HEC ✓ / ✗ / —** — the latest endpoint validation result, shown only for enabled destinations
- The queue pill — see below

The card body shows speed, gear, lap, lap time, and track, with the session's fastest lap in the top-right.

### The queue pill

The queue pill covers **outbound HEC and Observability requests only**. It is not the UDP receive path and does not report dropped game packets.

| Pill | Meaning |
| --- | --- |
| **QUEUE OK** | No outbound request was rejected for capacity in the last 10-second sample. This does not prove the destination accepted every request. |
| **Q 12/60** | This rig currently has 12 requests using a shared 60-request capacity. The denominator is shared across all rigs, not reserved per card. |
| **3 DROP** | Three outbound requests were rejected in the last 10-second sample because the shared in-memory capacity was full. |

HTTP and network delivery failures are recorded in the collector log and health data, and can occur even while the pill reads **QUEUE OK**.

## Entering a driver name

![Entering a driver name on a rig card](/assets/screenshots/f1-2025/driver-name.png)

1. Select **EDIT** on the rig card.
2. Type the driver's display name.
3. Select **SAVE**.

The name is a label attached to that rig's delivered telemetry. Saving a new name also clears the previous race-complete and fastest-lap display, which is how a card is handed over to the next driver.

## Recording

With collectors running on live UDP, press **RECORD** once to arm booth recording for every rig. The control then reads **ARMED** with a count of the rigs actively writing files. See [Running an Event](/f1-2025/managing-collectors/#recording-telemetry) for the full lifecycle.

The Record control is hidden while Playback Mode is enabled.

## Built-in help

Select **?** in the top-right corner for an operator reference with tabs for Start, Dashboard, Config, Health, and Logs.

![The built-in help panel](/assets/screenshots/f1-2025/help.png)

## Recommended first-use sequence

1. Open **Config**, set the rig count and an **Event Name**, and configure your [destinations](/f1-2025/controller-config/).
2. Select **Deploy Configuration**.
3. Turn on **Master Control** and confirm it reads **SYSTEMS LIVE**.
4. Configure the game using the collector address and the rig's UDP port.
5. Start a practice session and confirm the card shows **Telemetry live** with real values.
6. Confirm the destination pills on the card show **✓**.

{{< callout type="default" >}}

**One change at a time**

During setup, first prove UDP ingest, then prove HEC, then prove Observability. Separating the checks makes network and credential problems much easier to identify.
{{< /callout >}}
