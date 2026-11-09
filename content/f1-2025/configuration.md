---
title: "Using the v6 Collector"
linkTitle: "The Collector Page"
weight: 30
type: "docs"
---

The collector page is the operator screen for up to four independent rigs. The footer identifies the installed version. These instructions describe **v6.0.9**. The screenshots show a demonstration setup with destinations disabled.

![v6 collector with four independent rig cards](../images/v6/collector.webp)

## Status bar

| Pill | Meaning |
| --- | --- |
| **Event** | Event Name used to identify the event in Splunk. |
| **Game** | F1 2025, the UDP format this collector accepts. |
| **IP** | Public internet address. It reads Unavailable when that address cannot be determined. Use the host's LAN address for local rigs. |
| **Memory** | Collector-process memory, not the entire host or Docker VM. |
| **HEC / Observability** | Destination delivery status. Click to open that destination's health tab. |
| **Queue** | Outgoing batches waiting on disk. Click for queue health. |

**Connected** means delivery has succeeded and there is no current delivery problem; it does not verify dashboard results. **Waiting** means no successful delivery since startup. **Retrying** means a failed delivery is being retried. **Off** means disabled. A disabled destination with retained data is paused.

**Queue · Delayed** means data has waited longer than the configured warning threshold, normally 30 seconds. The threshold does not delete data.

## Rig cards

| Card state | Operator meaning |
| --- | --- |
| **Awaiting driver** | Enter the next attendee. No race is being collected. |
| **Driver required** | The game is sending data, but no driver is ready. Enter a name and select Ready before starting the race. |
| **Ready** (papaya) | Driver assigned; waiting for the first starting light. |
| **Collecting** (green) | Race telemetry is being accepted. |
| **Awaiting result** (cyan) | The race has ended. Leave the game running through the results screen while the collector waits for the result. |
| **Saving result** | The collector is saving the result. Wait until the card is ready for the next driver. |
| Warning / error | Select the pill to open the relevant activity log. |

**Listener · On** means the collector is ready to receive game data on that port. The **UDP** pill shows the rig’s configured port; use **Collector health → Rigs** to inspect incoming packet counts. An open listener alone does not mean a race is being captured.

Each card shows Rig, Fastest Lap (purple), Lap, Lap Time, Speed and Gear. After assignment, the driver’s name replaces the entry field. The bottom row retains the last result. **Saved locally** confirms the result was saved on the collector; check the delivery status to confirm it reached Splunk.

## Entering a driver name

1. Enter the attendee's display name in **Next driver** on the correct rig.
2. Select **Ready** before the game starts its lights.
3. Ask the attendee to start the race. Collection begins at the first starting light.

Names must contain **1–60 characters** using **A–Z, a–z, 0–9, ordinary spaces, underscores or hyphens**. Apostrophes, accents, slashes and other punctuation are not accepted. Leading/trailing spaces are trimmed; spaces inside the name remain in the UI and Splunk.

If the name is invalid, an explanation appears and **Ready** stays disabled until you correct it.

![Invalid name with inline guidance and Ready disabled](../images/v6/name-validation.webp)

See [Running an Event](/f1-2025/managing-collectors/) for the full race workflow.

## Top menu

| Button | Use |
| --- | --- |
| **Recordings** | Arm recording globally, upload/download files and play a race on an idle rig. |
| **Collector health** | Inspect Overview, Rigs, HEC, Observability and Queue. |
| **Logs** | Search and download the current run's activity history. The red badge counts unread warnings/errors. |
| **Configuration** | Set the event, rigs and destinations. |
| **?** | Tabbed help for race operation and each menu feature. |

![Tabbed operator help](../images/v6/help.webp)

## Recommended first-use sequence

Configure the event and destinations, verify **Listener · On**, configure the game's UDP address/port, then run a complete three-lap test race with a ready driver. Verify the final result and each enabled destination’s dashboard.
