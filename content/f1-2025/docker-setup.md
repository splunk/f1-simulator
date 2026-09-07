---
title: "Docker Setup for Local Use"
linkTitle: "Docker Setup"
weight: 20
type: "docs"
---

These instructions run the collector image on macOS or Linux.

{{< callout type="info" >}}

**Splunk Show users can skip this page**

Most events run on a requested Splunk Show instance, where the collector is already installed, running, and configured for {{< term "HEC" >}}. Go straight to [Collector Configuration](/f1-2025/controller-config/) instead.

{{< /callout >}}

## Prerequisites

- Docker Desktop or Docker Engine
- A Splunk HEC URL and token if sending full telemetry to Splunk
- A Splunk Observability Cloud {{< term "realm" >}} and access token if sending real-time metrics
- The computer's LAN IP address, reachable from the racing rig

{{% steps %}}

## Start the collector

Create the configuration file the container writes settings back into, then start the container:

```bash
touch "$HOME/config.json"
chmod 666 "$HOME/config.json"

docker run -d \
  --name f1-2025 \
  --restart always \
  -v "$HOME/config.json:/app/config.json" \
  -p 81:8501/tcp \
  -p 8501:8501/tcp \
  -p 20777:20777/udp \
  -p 20778:20778/udp \
  -p 20779:20779/udp \
  -p 20780:20780/udp \
  ghcr.io/splunk/f1-2025-go:latest
```

{{< callout type="default" >}}

**Collector repository users**

If you have the collector repository checked out, `./v5/scripts/start-collector.sh` performs exactly these steps, including removing any existing `f1-2025` container first.

{{< /callout >}}

## Check collector health

The container listens on TCP `8501`. The run above publishes it on both host port `81` and host port `8501`, so the UI is reachable at either address:

- [http://localhost:81](http://localhost:81) — matches the `:81` convention used by Splunk Show instances
- [http://localhost:8501](http://localhost:8501)

Confirm the container becomes `healthy`:

```bash
docker ps --filter name=f1-2025
```

{{< callout type="info" >}}

**Publishing UDP ports**

All four UDP ports are published above so that extra rigs can be enabled later without recreating the container. The collector only binds the ports for the rig count set under **Config → General**.

{{< /callout >}}

## Configure the collector

Open **Config** in the UI, set an **Event Name**, enable HEC and/or Observability, then select **Deploy Configuration**. Turn on **Master Control** to start collecting. See [Collector Configuration](/f1-2025/controller-config/) for field details.

{{< callout type="warning" >}}

**An event name is required**

Master Control refuses to start until an event name is set. The error reads `Event name is not configured.`

{{< /callout >}}

## Connect the racing rig

Follow [Game Telemetry Setup](/f1-2025/telemetry/) to configure F1 25 with the collector address and UDP port. Run a short practice session and confirm live values appear on the rig card.

{{% /steps %}}

## Persistent files

| Container path | Purpose |
| --- | --- |
| `/app/config.json` | Collector settings, including destination URLs and tokens |
| `/app/telemetry_data` | `.tlm` recordings and bundled replay files |
| `/app/collector.log` | Rotating collector log (10 MB, three backups) |

The run command above bind-mounts `$HOME/config.json`, so settings survive container replacement. Recordings do not unless you also mount the data directory:

```bash
-v "$HOME/f1-telemetry:/app/telemetry_data" \
```

Mount it before an event if the `.tlm` files must be kept. Note that this mount also replaces the bundled replay files used by [Playback Mode](/f1-2025/controller-config/#playback-mode), so copy any replay you want to keep using into the host directory.

## Useful commands

```bash
# Follow collector logs
docker logs -f f1-2025

# Restart the collector
docker restart f1-2025

# Stop and remove the container; the mounted config file is retained
docker rm -f f1-2025

# Pull a newer image before recreating the container
docker pull ghcr.io/splunk/f1-2025-go:latest
```

## Network access

Allow inbound TCP `81` (or `8501`) from the operator network and inbound UDP `20777` from the racing rig. Open the additional UDP ports only when additional rigs are enabled. For an internet-hosted collector, apply the same rules to the cloud firewall or security group.

## Next steps

1. [Configure the collector](/f1-2025/controller-config/)
2. [Configure F1 25 telemetry](/f1-2025/telemetry/)
3. [Run a pre-event health check](/f1-2025/monitoring/#pre-event-checklist)
