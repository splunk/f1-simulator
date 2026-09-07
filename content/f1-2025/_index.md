---
title: "F1 2025 Data Collector"
linkTitle: "F1 2025 Collector"
weight: 10
type: "docs"
sidebar: {"open": true}
cascade: {"type": "docs"}
---

The F1 2025 Collector receives {{< term "UDP" >}} telemetry from up to four racing rigs and sends it to Splunk Enterprise or Splunk Cloud through HTTP Event Collector ({{< term "HEC" >}}). It can also send a focused set of real-time metrics to Splunk Observability Cloud.

![F1 2025 Collector](/assets/screenshots/f1-2025/collector.png)

The collector is a single Go application. One process serves the web interface, listens on every rig's UDP port, and delivers to both destinations, so there are no separate listener, queue, or database services to manage.

The default setup uses one rig on UDP port `20777`. Additional rigs can be enabled from the collector when an event needs them.

## Two views

| View | Path | Purpose |
| --- | --- | --- |
| **Collector** | `/` | The operator screen. Master Control, rig cards, driver names, recording, configuration, health, and logs. |
| **Pit Wall** | `/pitwall` | A broadcast-style live telemetry view for a single rig, suitable for a display screen behind the booth. |

## Choose your setup

{{< tabs >}}
{{< tab name="Splunk Show" >}}


This is how most events run. Your Show instance already has the collector installed, running, and configured for HEC. Do not replace the HEC URL or token unless your event administrator asks you to.

1. Open `http://<your-show-host>.splunk.show:81`.
2. Confirm an **Event Name** is set under **Config → General**.
3. Configure only your [Splunk Observability Cloud destination](/f1-2025/controller-config/#splunk-observability-cloud), if you are using it.
4. Select **Deploy Configuration**, then turn on **Master Control**.
5. Copy the collector's public address from the header into F1 25 and use UDP port `20777` for the first rig.
6. Enter the driver's name on the rig card before their race.

{{< /tab >}}
{{< tab name="Run locally" >}}


Run the collector with Docker on macOS or Linux, then configure your own HEC and/or Observability destination.

1. Follow [Docker Setup](/f1-2025/docker-setup/).
2. Open `http://localhost:81`.
3. Configure [an event name and your destinations](/f1-2025/controller-config/).
4. Configure [F1 25 UDP telemetry](/f1-2025/telemetry/).
5. Enter the driver's name on the rig card.

{{< /tab >}}
{{< /tabs >}}

## Event workflow

1. Open **Config**, set the number of rigs and an **Event Name**, and enable the destinations you need.
2. Select **Deploy Configuration**. This writes the configuration file and stops any running collectors.
3. Turn on **Master Control**. The collector validates every enabled destination before it starts; a failed check prevents startup and shows the reason.
4. Configure each game to use the collector's address and that rig's UDP port.
5. Enter the driver's name on the correct rig card before their race.
6. Run the event. When F1 25 sends **Final Classification**, the collector marks the rig **Race complete** and emits a `SessionCompleted` summary containing the session's fastest lap.
7. If Final Classification never arrives, the collector falls back to **Session Ended** after a 60-second grace period and publishes the summary from cached data.

{{< callout type="default" >}}

**Test before guests arrive**

Run one complete short race, including the results screen, before the event. This checks UDP reception, destination delivery, and automatic session completion in one pass.

{{< /callout >}}

## Next steps

{{< cards cols="2" >}}
{{< card link="./configuration/" title="The Collector page" subtitle="Understand rig cards, driver names, recording and status." >}}
{{< card link="./controller-config/" title="Configure the collector" subtitle="Set your event name, destinations and playback mode." >}}
{{< card link="./telemetry/" title="Connect F1 25" subtitle="Point each racing rig at the right address and UDP port." >}}
{{< card link="./managing-collectors/" title="Run an event" subtitle="Manage drivers, recordings and race completion." >}}
{{< card link="./pit-wall/" title="Use the Pit Wall" subtitle="Show a single rig’s live telemetry on a booth display." >}}
{{< card link="./monitoring/" title="Monitor and troubleshoot" subtitle="Check health, read logs and diagnose common problems." >}}
{{< card link="./dashboards/" title="Explore your dashboards" subtitle="View telemetry in Splunk and Observability Cloud." >}}
{{< /cards >}}
