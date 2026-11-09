---
title: "Running an Event"
linkTitle: "Running an Event"
weight: 50
type: "docs"
---

Prepare the game using the [Event Guide](/event_guide/). The collector handles up to four independent rigs; it does not create or advance the game playlist.

## Before a driver starts

1. Confirm the correct rig shows **Listener · On** and there are no storage/configuration errors.
2. Enter the attendee's name under **Next driver**.
3. Select **Ready**. The card becomes papaya and shows **Current driver**.
4. Ask the driver to select **Start Race** in the game.

The collector starts collecting the attendee’s race data at the first starting light. Select **Ready** before the lights appear. Game data arriving before the race or without a ready driver does not count as a captured race.

## During a session

The card becomes green while collecting and shows lap, lap time, speed, gear and fastest valid lap. Recording raw `.tlm` files is optional and separate from normal delivery to Splunk.

If the first light was missed, use **Abort / reset**, assign the driver again, and restart the race.

## Completing a session

1. When the race ends, the card may show **Awaiting result**. Leave the game running through the results screen.
2. Wait while the collector saves the result. If recording is on, the race file closes when the result arrives.
3. Once saving succeeds, the card opens for the next driver, even if a destination is temporarily offline. The last result stays at the bottom of the card.

A **DNF** keeps the fastest known valid completed lap before retirement. With no valid completed lap, there is no fastest time. Leave the game running through the results screen after a DNF too.

### If the result does not appear {#if-final-classification-never-arrives}

Leave the game running through its results screen and check **Logs** for a problem. The collector will not automatically complete a race just because the game stopped sending data. If the race has been abandoned and the result will not arrive, select **Abort / reset** and confirm **Abort attempt**. This saves an incomplete outcome rather than a completed result.

If the card is saving a received final result, resolve the storage problem and let it finish; abort is blocked while completion is being saved. After a restart, follow the displayed recovery state rather than starting the same heat again blindly.

## Recording telemetry

![Global recording control](../images/v6/recording.webp)

1. Open **Recordings → Recording** and turn on **Record all rigs** before the next race.
2. Assign each driver normally. Each rig saves its own race file, from the first starting light until the result arrives.
3. Leave the switch on across driver changes. The armed indicator means future races will be recorded.
4. Turning the switch off lets active recordings finish. Turning it on mid-race applies to the next race.

Abort, shutdown or a recording failure can leave an incomplete diagnostic file. Optional recording failure does not stop normal Splunk delivery. A restart does not resume an open recording.

### Saved files, import and export

![Saved recordings with download and delete icons](../images/v6/saved-files.webp)

In **Recordings → Saved files**, use the **download icon** to export a `.tlm`, or choose a file and select **Upload recording** to import recordings. Only complete races, from the starting lights through the result, are playable. Incomplete files remain downloadable for investigation. The trash icon deletes a finished file after confirmation; active files are protected.

New race recordings include the assigned driver in their download filename, for example `20261006_170000_f1-2025_Rig_1_Alex_Taylor.tlm`. Spaces become underscores in the filename only; the displayed/Splunk name remains `Alex Taylor`. Existing recordings and imported filenames are unchanged.

Files remain under `/data/recordings` until deleted. Storage settings default to a 32 GiB library, 500 MiB maximum upload and 1 GiB free-space reserve. Export recordings you need before deleting the Docker volume or terminating a disposable instance. Recordings can contain data for other cars and in-game names. The separate driver and event details are not embedded in the exported file.

## Playback

![Per-rig playback selection](../images/v6/playback.webp)

1. Open **Recordings → Playback** and choose a saved race and an idle rig. Only recordings for the selected game are listed.
2. For a single replay, enter a driver name. To repeat the race with generated names, turn on **Loop** instead.
3. Select **Start playback**. Playback runs at normal speed and sends data to the configured destinations. Other rigs can continue operating; the selected rig cannot collect a live race during playback.

The driver name follows the [same rules as a live race](/f1-2025/configuration/#entering-a-driver-name). Playback does not create a new recording or resume after a restart.

The rig’s status pill shows playback progress and elapsed/total time in minutes and seconds. **Stop playback** aborts an unfinished replay. If the result has already arrived, stopping preserves it while it saves.

Playback can appear on dashboards and leaderboards. Use a test destination or [filter it out](/f1-2025/dashboards/#playback-data). There is no pause or seek. A loop also stops if the delivery queue cannot accept another race or all generated names have been used.

## Adding rigs

Before assigning drivers, open **Configuration → Rigs**, add up to four rigs and save. Match each game's UDP port to its rig; publish the ports in Docker and allow them through the firewall. Standard assignments are `20777`–`20780`.
