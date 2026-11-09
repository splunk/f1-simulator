---
title: "Viewing F1 2025 Data"
linkTitle: "Dashboards"
weight: 90
type: "docs"
---

Use the dashboards below to view race data sent to your configured Splunk destinations.

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

## Completed race results {#session-summary-events}

After the race, leave the game running through the results screen. The collector saves the result and sends a fastest-lap summary to Splunk. If the result does not appear, check the collector card and [troubleshooting guide](/f1-2025/monitoring/).

## Playback data

Playback goes to the configured destinations and may appear in your dashboards. Use a separate test destination or ask your dashboard administrator to filter out playback data (`data_mode=playback`) from conference results.

## Validate the data first

1. Confirm the driver was Ready before the first starting light and the card collected the race.
2. Check the relevant destination pill and health tab.
3. Verify its queue drains and inspect Logs for errors.
4. Check the dashboard's index, event, rig and time-range filters.
5. Confirm the game reached its results screen and the collector saved the result.

**Connected** is a successful delivery indicator, not a guarantee that a particular dashboard query matches the data. Health exports may be arriving even when no race has been captured.
