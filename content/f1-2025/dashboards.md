---
title: "Viewing F1 2025 Data"
linkTitle: "Dashboards"
weight: 90
type: "docs"
---

The collector feeds full telemetry events to Splunk Enterprise or Splunk Cloud through HEC, and a smaller real-time metric set to Splunk Observability Cloud.

## Splunk Observability Cloud

A pre-built F1 2025 dashboard group is available in the repository.

1. Download the [F1 2025 Observability dashboard group](https://github.com/splunk/f1-simulator/blob/main/observability/dashboard_group_F1_2025.json).
2. In Splunk Observability Cloud, open **Dashboards**.
3. Select **Create → Import**.
4. Upload the JSON file and import it.
5. Open the **F1 2025** dashboard group.

If charts are empty, check the **Observability** delivery pill and verify the realm/token under **Configuration → Observability**.

## Splunk Enterprise and Splunk Cloud

The [Data Drivers app](https://github.com/splunk/datadrivers-app) provides the F1 2025 dashboards.

For a standalone environment:

1. Download or clone the app repository.
2. Package the `datadrivers-app` directory as a `.tar.gz` file.
3. In Splunk, open **Apps → Manage Apps → Install app from file**.
4. Upload the package and follow the restart prompt if shown.
5. Open **Data Drivers – F1 2025** from the Apps menu.

For managed Splunk Cloud or a centrally administered Splunk deployment, ask the platform administrator to install the app using the organization's normal application deployment process.

The collector does not choose an index. Events land in whatever index the HEC token is configured for — normally `data_drivers_f1_2025`. If searches return nothing, confirm the token's index with your Splunk administrator.

## Session summary events

For each completed attempt, v6 queues a `SessionCompleted` summary alongside the attendee's Final Classification event. It uses `packet_id=97`, `summary_type=fastest_lap`, `completion_source=final_classification` and `final_classification_received=true`. There is no SEND timeout fallback.

HEC fields include `source=f1_2025`, hosts `rig_1`–`rig_4`, `custom_event` (Event Name), `player_name` and `best_lap_time_in_ms`. v6 adds `attempt_id`, `record_id` and `data_mode`. Identical driver names can have separate attempts. Delivery is at least once; deduplicate retries by `record_id`.

Example conference leaderboard (substitute your HEC token's index):

```spl
index=data_drivers_f1_2025 source=f1_2025 sourcetype=SessionCompleted
custom_event="Data Drivers" data_mode=live best_lap_time_in_ms>0
| dedup record_id
| stats min(best_lap_time_in_ms) as best_lap_ms latest(player_name) as player_name by attempt_id host
| sort 0 best_lap_ms
| eval best_lap_seconds=round(best_lap_ms/1000,3)
| table player_name best_lap_seconds host
```

## Playback data

Managed playback goes to the configured destinations. HEC events carry `data_mode=playback`; playback Observability metrics add the same dimension. Filter it out of conference results or use a separate test destination. Live Observability dimensions are `f1.hostname`, `f1.gameVersion` and `f1.eventName`.

## Validate the data first

1. Confirm the driver was Ready before STLG 1 and the card collected the race.
2. Check the relevant destination pill and health tab.
3. Verify its queue drains and inspect Logs for errors.
4. Check the dashboard's index, event, rig and time-range filters.
5. Confirm Final Classification arrived for a completed-race result.

**Connected** is a successful delivery indicator, not a guarantee that a particular dashboard query matches the data. Health exports may be arriving even when no race has been captured.
