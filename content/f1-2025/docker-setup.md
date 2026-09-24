---
title: "Docker Setup for Local Use"
linkTitle: "Docker Setup"
weight: 20
type: "docs"
---

These instructions run **v6** on Docker Desktop or Docker Engine. Splunk Show users with v6 already provisioned can go straight to [Collector Configuration](/f1-2025/controller-config/).

## Prerequisites

- Docker and a release image built for the host architecture (ARM64 or AMD64).
- HEC URL/token and/or an Observability realm/token.
- A reachable collector IP address and the required TCP/UDP firewall rules.

## Start the collector

The standard deployment uses the published `ghcr.io/splunk/f1-2025-v6:latest` image. `latest` follows new releases; use a tested version tag or digest if you need to control exactly when an event deployment changes.

Save this as your collector startup script. The **named volume mounted at `/data` is required to retain configuration across container replacements**.

If an existing collector was started without a named volume, follow [migration](#migrate-an-existing-collector) **before** running this script. Creating a named volume does not copy the previous volume's contents.

```bash
#!/bin/bash
set -euo pipefail

IMAGE="ghcr.io/splunk/f1-2025-v6:latest"
DATA_VOLUME="f1-v6-data"

docker volume create "$DATA_VOLUME" >/dev/null
docker pull "$IMAGE"

if docker container inspect f1-2025 >/dev/null 2>&1; then
    docker stop --timeout 120 f1-2025
    docker rm f1-2025
fi

docker run -d \
  --name f1-2025 \
  --restart always \
  --stop-timeout 120 \
  --read-only \
  --cap-drop ALL \
  --security-opt no-new-privileges:true \
  --mount "type=volume,source=$DATA_VOLUME,target=/data" \
  -p 81:8501/tcp \
  -p 8501:8501/tcp \
  -p 20777:20777/udp \
  -p 20778:20778/udp \
  -p 20779:20779/udp \
  -p 20780:20780/udp \
  "$IMAGE"
```

To build locally from the [collector repository](https://github.com/splunk/datadrivers-f1-collector):

```bash
./v6/scripts/build.sh --version keep --tag none --local \
  --repository f1-2025-v6 --yes
```

Use the exact local tag printed by the build script in place of the published image. Local builds do not publish an image.

Run only one collector on each set of published ports.

## Check collector health

Open `http://localhost:81` or `http://localhost:8501`. From another machine, substitute the collector host address. Both ports above map to the same UI/API service. Check:

```bash
docker ps --filter name=f1-2025
curl --fail http://localhost:81/healthz
```

The container should become healthy. Healthz confirms the process responds, not that data is visible in Splunk.

## Configure the collector

Open **Configuration**, set the event and rigs, enable HEC and/or Observability, then **Save configuration**. Save before using **Test saved connection**. Listeners start automatically. Driver assignment requires at least one configured, enabled destination.

## Connect the racing rig

Follow [Game Telemetry Setup](/f1-2025/telemetry/). Enter a test driver and select Ready, then run a three-lap Grand Prix through Final Classification. A practice session without a first-light event does not test v6 race capture.

## Persistent files

Mount **one writable `/data` volume per collector instance**. It holds:

| Path | Purpose |
| --- | --- |
| `/data/config.json` | Saved configuration and destination secrets |
| `/data/recordings` | Raw recordings, metadata and recording settings |
| `/data/results` | Local race outcomes |
| Other `/data` state | Durable destination queues, rig recovery/completion state and collector identity |
| `/opt/collector/telemetry_data` | Read-only bundled sample recordings in the image |

No separate configuration bind mount is needed. Configure the collector through its UI or supported HEC update API. Keep the volume when replacing the container. Never run two collectors against the same data directory.

Two bundled Austria recordings are imported into Saved files on startup without starting playback. Deleting an imported sample keeps it deleted on later starts; upload it again to restore it.

## Verify persistence

```bash
docker inspect f1-2025 \
  --format '{{range .Mounts}}{{println .Name "->" .Destination}}{{end}}'
```

Expect `f1-v6-data -> /data`. Both UI changes and `/update_hec` updates are stored in this volume. Reusing the same volume preserves configuration, pending delivery, recordings and results. Do not delete it when replacing the container.

### Migrate an existing collector

Finish all assigned races and pause automatic updates during migration. Inspect the current `/data` mount before removing the old container. An installation without an explicit mount normally has an anonymous Docker volume with a long generated name.

Stop the collector gracefully, back up its complete `/data` directory, and copy its contents into the new named volume. Preserve ownership and file permissions; the collector runs as UID/GID `10001`. Then start the replacement with `f1-v6-data:/data` and verify configuration and retained recordings/results before discarding the old volume or backup. Do not copy a live, changing queue.

If starting with an empty volume is intentional, configure destinations once after switching. An earlier anonymous volume may still contain lost settings unless it was deleted. Mounting only `/app/config.json` does not persist v6 configuration; its active path is `/data/config.json`.

### Watchtower and EC2

Watchtower replacements must retain the named `/data` mount. Its `--remove-volumes` / `WATCHTOWER_REMOVE_VOLUMES` option targets anonymous volumes, not named volumes. See [Watchtower's volume option](https://github.com/containrrr/watchtower/blob/main/docs/arguments.md#remove-anonymous-volumes) and [Docker volume persistence](https://docs.docker.com/engine/storage/volumes/).

A named volume survives container replacement on the same host. It does not by itself survive deletion of the EC2 disk. For a disposable event host, drain both destination queues and export wanted files before termination. Schedule image updates between races; persistence does not make a container restart transparent to an active race.

## Useful commands

```bash
# Follow process logs
docker logs -f f1-2025

# Graceful stop (allow accepted data to flush)
docker stop --timeout 120 f1-2025

# Start the same container again
docker start f1-2025
```

For upgrades, finish assigned races, check destination queues, stop gracefully, then replace the container using the same data volume and a tested image. If storage is failing, restore it or extend the stop timeout; forced termination can lose unwritten memory.

Before deleting a volume or terminating EC2, verify both queues are empty and download any recordings/logs you want to keep.

## Network access

Restrict TCP `81`/`8501` to trusted operators/automation; the UI and configuration APIs are not a public multi-user authentication service. Allow UDP `20777`–`20780` from the relevant rigs. Publish only the additional ports your deployment needs. Outbound connectivity must reach configured destinations; public-IP lookup failure does not stop capture.

## Next steps

1. [Configure the collector](/f1-2025/controller-config/)
2. [Configure F1 25 telemetry](/f1-2025/telemetry/)
3. [Run the pre-event checklist](/f1-2025/monitoring/#pre-event-checklist)
