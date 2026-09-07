---
title: "Pit Wall"
linkTitle: "Pit Wall"
weight: 70
type: "docs"
---

The **Pit Wall** at `/pitwall` is a broadcast-style live telemetry view for a single rig. It is designed for a display screen behind the booth rather than for the operator.

![The Pit Wall view during a session](/assets/screenshots/f1-2025/pit-wall.png)

## Using it

1. Open **Pit Wall** from the navigation.
2. Choose the rig to follow from the selector in the header.
3. Select **STREAM**.

The driver's name is shown at the top right. **STOP** ends the stream; changing the selected rig switches which car is displayed.

The Pit Wall requires a tablet or desktop browser. On narrow screens it shows a message instead of the layout.

## What it shows

| Panel | Contents |
| --- | --- |
| **Race Status** | Track name, lap, sector, position, DRS state |
| Track map | The car's path around the circuit with live sector timing |
| Speed gauge | Current speed in the configured display unit |
| **Weather** | Condition, air and track temperature, rain percentage |
| Car view | Per-corner tyre and brake temperatures |
| **Engine Temp** / **RPM** | Live bar readouts |
| **Shift Lights** / **Gear** | Current shift-light state and selected gear |
| **Speed** / **Throttle** / **Brake** | Rolling charts with current, highest, and average values, plus ERS mode |
| Lap timing | Current lap, best lap, and S1/S2/S3 sector times |

## Notes

- The Pit Wall reads the same telemetry stream as the Collector page. It does not change what is delivered to Splunk, and streaming to it is not required for collection.
- It works identically with [Playback Mode](/f1-2025/controller-config/#playback-mode), which makes it a good way to test a booth display before an event.
- Speed follows the **Speed Display** setting under [Config → General](/f1-2025/controller-config/#general).
