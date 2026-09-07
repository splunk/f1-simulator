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

If charts are empty, confirm the rig cards show **O11y ✓** and verify the realm and access token under **Config → Destinations**.

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

In addition to the raw parsed packets, the collector emits one `SessionCompleted` event per completed session, carrying that session's fastest lap. It is correlated by rig and the game's session UID, and is the most convenient event to build leaderboards from — it avoids scanning every lap record.

Useful fields include `completion_source` and `final_classification_received`, which indicate whether the summary came from the authoritative Final Classification packet or from the 60-second Session Ended fallback.

## Validate the data first

Before troubleshooting a dashboard, confirm delivery at the collector:

1. **Master Control** reads **SYSTEMS LIVE**.
2. The rig card shows **HEC ✓** or **O11y ✓** for the destination you are querying.
3. The queue pill reads **QUEUE OK**.
4. The **Logs** panel shows no repeating delivery errors.
5. The rig is producing live values.

{{< callout type="default" >}}

**Keep dimensions predictable**

Use consistent event names and rig names throughout an activation. This makes filters reusable and prevents one physical rig from appearing as several unrelated time series.
{{< /callout >}}
