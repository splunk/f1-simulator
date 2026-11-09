---
title: "Monitoring and Troubleshooting"
linkTitle: "Monitoring and Troubleshooting"
weight: 60
type: "docs"
---

Check game reception, race progress and destination delivery separately. An open listener alone does not mean a race is being captured or that Splunk has received it. In **Collector health → Rigs**, check that the packet count increases while the game is sending data.

## Pre-event checklist

- Confirm the expected v6 image/version and a healthy container.
- Confirm **Event**, rig ports and **Listener · On** on every rig.
- Test each saved destination you intend to use.
- Run a complete three-lap race on every rig at normal speed, entering a driver and selecting Ready before the first light.
- Leave the game running through the results screen. Check that the collector saves the correct fastest lap and opens the card for the next driver.
- Verify the race data and driver/event filters in your dashboards.
- Check that the enabled destinations’ queues clear and there are no storage errors.
- If recording is needed, arm it, then download and test a completed file.

## Collector Health

![Collector health overview](../images/v6/health.webp)

**Collector health** refreshes every five seconds and has one row of tabs:

| Tab | What to inspect |
| --- | --- |
| **Overview** | Process uptime, memory, CPU and runtime diagnostics. |
| **Rigs** | Whether each listener is running and receiving data, plus race and error counts. |
| **HEC** | Delivery attempts, failures, latency, last delivery and errors. |
| **Observability** | Independent metric delivery status and errors. |
| **Queue** | Data waiting for delivery, its age, available storage and health exports. |

![Queue configuration](../images/v6/queue.webp)

**Filtered** counts data the collector deliberately ignores, such as data received before a driver is ready. It does not measure lost network data. **Health samples skipped** means optional health updates were skipped to preserve space for race data.

Health counters generally reset when the collector or a listener restarts.

### Health data in Splunk

Health export is enabled by default. Configure it and its interval under **Configuration → Queue**. The local health view still works if export is disabled.

## Logs

![Searchable collector activity log](../images/v6/logs.webp)

Open **Logs**, or select a rig status/listener/UDP pill for that rig's history. Filter by rig/destination and severity, or search driver/message text. Use the download icon to export retained entries as JSON.

The latest **1,000 entries** are held in memory for the current run; they reset on restart and are not forwarded to Splunk. Repeated messages can be grouped with a **×N** badge. The red badge tracks unread warnings and errors. Export before restarting when investigating a problem. Container logs are also available with `docker logs -f f1-2025` (substitute your container name).

## Common problems

| Symptom | Action |
| --- | --- |
| **Driver required** or first light missed | Enter the name and select **Ready** before starting. If the lights have passed, use **Abort / reset**, assign the driver and restart the race. |
| **Awaiting result** | Leave the game running through the results screen and wait for the collector to save the result. |
| **Saving result** / storage error | Check free space, volume writability and Queue health. Let local saving recover; do not force a duplicate heat. |
| Listener failed | Check for another process using the UDP port, correct Configuration → Rigs and save to retry. |
| Delivery retrying | Check destination health and logs, URL scheme/port, token, realm and network reachability. |
| Queue delayed | Restore delivery and watch each destination drain. Raising the warning threshold does not fix the outage. |
| Status unavailable | Browser cannot confirm the collector's current state. Check the container/network; do not rely on stale card values. |

### Configuration missing after an update

Verify that `f1-v6-data` is mounted at `/data`; creating a replacement without reusing storage starts with fresh settings. See [persistent storage and Watchtower](/f1-2025/docker-setup/#verify-persistence). Do not delete old anonymous volumes before checking whether they contain the missing configuration.

### The collector is not receiving game data {#no-udp-packets}

Confirm F1 25 UDP Telemetry On, Broadcast Off, format 2025, correct collector address and unique rig port. Check Docker UDP publishing, host firewall/cloud security group and any configured source-IP restriction. The public IP pill is not the address to use for a LAN-only collector.

### The game is connected but dashboards are empty {#packets-arrive-but-no-events-are-delivered}

First distinguish reception from capture: select **Ready** before the first starting light. Then check the destination is enabled, its saved connection test succeeds and its queue is progressing. The HEC token selects the index. Check event-name and time-range filters in dashboards.

### Delivery errors while no one is racing

Health updates are sent between races, so delivery errors can appear even when no one is racing. Check the destination settings and network connection; the collector retries queued data.

## Queue retention and shutdown

Unsent batches are stored independently per destination on `/data`. They survive container restarts with the volume preserved and do not expire after 30 seconds. Occasionally a retry can result in duplicate data in Splunk.

Stop the collector gracefully so it can finish saving data. If storage is unavailable, resolve the problem before forcing it to stop; a forced stop or power loss can lose data that has not yet been saved.

Before terminating a disposable EC2 instance, check **all enabled destination queues are empty** and export any wanted recordings/logs. A locally saved result or a healthy container is not proof that every queued batch is already in Splunk.
