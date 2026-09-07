---
title: "Running an Event"
linkTitle: "Running an Event"
weight: 50
type: "docs"
---

Every enabled rig is independent. Recording and race completion on one rig do not affect another.

## Before a driver starts

1. Confirm the rig card shows **Telemetry live** or **Awaiting telemetry**, not **Collector stopped**.
2. Select **EDIT** on the card.
3. Enter the driver's display name and select **SAVE**.
4. Ask the driver to start or join the configured F1 25 session.

The driver name is a label carried with that rig's delivered telemetry. Unlike earlier collector versions, it is not a lock: packets arriving before a name is entered are still parsed and delivered, attributed to whatever name the rig currently holds. Set the name **before** the race rather than during it.

Saving a name also clears the previous race-complete state and fastest lap from the card, which is how you hand a rig over between drivers.

## During a session

Watch the rig card for speed, gear, lap, lap time, and track. If the values stay blank, use [Collector Health](/f1-2025/monitoring/#collector-health) to determine whether packets are reaching the port.

## Completing a session

At the end of a normal race, let the driver reach the results screen so the game sends **Final Classification**. On receipt, the collector:

- marks the card **Race complete**;
- stops that rig's active recording;
- forwards the original Final Classification event to HEC; and
- emits a `SessionCompleted` summary event containing the session's fastest lap.

{{< details title="How the session summary chooses a fastest lap" closed="true" >}}

`SessionCompleted` is correlated by rig and the game's own session UID. The fastest lap is taken from Final Classification, which is authoritative; a matching personal fastest-lap event and then session history data are used as fallbacks.

{{< /details >}}

### If Final Classification never arrives

{{< details title="Automatic fallback after a game exit or crash" closed="true" >}}

If the game exits or crashes before the results screen, the collector waits 60 seconds after Session Ended and then publishes the summary from cached data, marked `completion_source=session_ended_fallback` with `final_classification_received=false`.

No operator action, PIN, or override is needed — this is automatic. A late Final Classification packet can still publish a higher-authority revision of the same summary.

{{< /details >}}

## Recording telemetry

Recording uses a booth model: one global arm control, and an independent recording lifecycle per rig.

1. With collectors running on live UDP, press **RECORD** once. The control changes to **ARMED**.
2. Each rig opens its own `.tlm` file when that simulator sends the five start lights.
3. A rig closes its own file on Final Classification, or on its own 60-second Session Ended fallback. The booth stays armed, so a rig that has finished can record the next race while other rigs are still running.
4. Press **ARMED** to immediately close every active recording and return to idle.

Files are written to `/app/telemetry_data` inside the container as `<timestamp>_<track>_<rig>.tlm`.

{{< details title="Recording interruptions and errors" closed="true" >}}

- If a game closes or telemetry disappears mid-race, 30 seconds of inactivity closes that rig's partial file without marking the race complete and without disarming the booth.
- A card showing **REC ERROR** could not create or write its file. Hover the pill for the error.
- Shutting down the collector or deploying configuration closes all open files.
{{< /details >}}

{{< callout type="warning" >}}
**Keep recordings across container replacement**

Recordings are lost when the container is replaced unless `/app/telemetry_data` is mounted — see [Persistent files](/f1-2025/docker-setup/#persistent-files).
{{< /callout >}}

{{< callout type="default" >}}

**Record a known-good race**

Keep a short, complete recording from a tested rig. Played back through [Playback Mode](/f1-2025/controller-config/#playback-mode), it validates dashboards and destinations without occupying the simulator.

{{< /callout >}}

## Adding rigs

Open **Config → General**, choose the required number of rigs, and deploy. Make sure the corresponding UDP ports are published by Docker or allowed by the cloud firewall. Each game uses the same collector address but a different port.

Return to one rig after a multi-rig event if that is the normal deployment. Fewer open ports and fewer unused cards make operation clearer.
