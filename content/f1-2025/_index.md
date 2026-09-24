---
title: "F1 2025 Data Collector"
linkTitle: "F1 2025 Collector"
weight: 10
type: "docs"
sidebar: {"open": true}
cascade: {"type": "docs"}
---

These guides cover the **v6 F1 2025 collector**: one Go service, up to four independent rigs, and delivery to Splunk Enterprise/Cloud through {{< term "HEC" >}}, Splunk Observability Cloud, or both. v6 is undergoing production field testing; verify your deployment before guests arrive.

![The v6 operator screen](/assets/screenshots/f1-2025/v6/collector.png)

Only the attendee's car is exported during the race window: **Ready → first starting light (STLG 1) → Final Classification**. Session Ended (SEND) means wait for the result; it does not complete the heat. Unsent data stays in a disk queue until delivered.

## Choose your setup

{{< tabs >}}
{{< tab name="Splunk Show" >}}

1. Open `http://<your-show-host>.splunk.show:81` and confirm the footer shows v6.
2. Check **Configuration → Event** and **Rigs**.
3. Keep provisioned HEC settings unless your administrator directs otherwise. Add your Observability realm/token if needed.
4. Save changes and test each saved destination.
5. Configure each game's UDP address and unique rig port.
6. Enter a driver name and select **Ready** before starting the race.

{{< /tab >}}
{{< tab name="Run locally" >}}

1. Follow [Docker Setup](/f1-2025/docker-setup/), including a persistent `/data` volume.
2. Open `http://localhost:81` or `http://localhost:8501`.
3. Configure the event, rigs and at least one destination.
4. Follow [Game Telemetry Setup](/f1-2025/telemetry/), using the Docker host's LAN IP for a separate simulator.
5. Enter a driver name and select **Ready** before starting the race.

{{< /tab >}}
{{< /tabs >}}

## Event workflow

Prepare 27 three-lap Grands Prix in the game. For each attendee, enter their name on the correct rig, select Ready, then ask them to start. Capture starts at the first light. After SEND, leave the game running until Final Classification arrives and the result is saved. The card then opens for the next driver. Rigs progress independently.

The container starts listeners automatically; v6 has no Master Control switch. The optional global **Record all rigs** switch saves raw files independently of sending data to Splunk. Per-rig playback runs once at normal speed.

## Test before guests arrive

Run a full three-lap race on each rig, including the results screen, and verify both destination dashboards. Check queue recovery after an interruption. Empty both queues and export wanted recordings before terminating a disposable host.

## Next steps

{{< cards cols="2" >}}
{{< card link="./configuration/" title="The Collector page" subtitle="Understand cards, pills and the top menu." >}}
{{< card link="./controller-config/" title="Configure the collector" subtitle="Set the event, rigs, destinations and queue." >}}
{{< card link="./telemetry/" title="Connect F1 25" subtitle="Choose the right game address and UDP port." >}}
{{< card link="./managing-collectors/" title="Run an event" subtitle="Manage drivers, record, import, export and replay." >}}
{{< card link="./monitoring/" title="Monitor and troubleshoot" subtitle="Check health, logs and durable delivery." >}}
{{< card link="./dashboards/" title="Explore your dashboards" subtitle="View race data in Splunk and Observability Cloud." >}}
{{< /cards >}}

## Deployment and automation

Use the [Docker instructions](/f1-2025/docker-setup/#persistent-files) for persistent storage and the [HEC update API](/f1-2025/controller-config/#automation) for provisioning. See [Display Screens](/f1-2025/pit-wall/) for spectator dashboards.
