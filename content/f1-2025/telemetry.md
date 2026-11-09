---
title: "F1 2025 Telemetry Configuration"
linkTitle: "Game Telemetry Setup"
weight: 80
type: "docs"
---

Configure every racing rig to send F1 25 {{< term "UDP" >}} telemetry to the collector.

{{% steps %}}

## Find the collector address

Choose the address the game can use to reach the collector. The **IP** pill shows the collector’s public address, which may differ from its local network address.

- **Splunk Show or cloud deployment:** use the address provided for your deployment, often the public address shown in the status bar.
- **Local Docker:** use the Docker host's LAN address, not `localhost`, because the game runs on another computer.
- **Same computer:** `127.0.0.1` can be used only when F1 25 and the collector run on the same machine.

## Configure F1 25

On the racing rig:

1. Launch F1 25.
2. Open **Game Options → Settings → Telemetry Settings**.
3. Configure:

| Setting | Value |
| --- | --- |
| UDP Telemetry | **On** |
| UDP Broadcast Mode | **Off** |
| UDP IP Address | The collector address |
| UDP Port | `20777` for RIG 1 |
| UDP Send Rate | **10Hz** |
| UDP Format | **2025** |
| Your Telemetry | **Restricted** |
| Show Online IDs | **Off** |

![F1 25 telemetry settings](../images/telemetry.webp)

## Multiple rigs

All rigs use the same collector address but a unique UDP port:

| Rig | UDP port |
| --- | ---: |
| RIG 1 | 20777 |
| RIG 2 | 20778 |
| RIG 3 | 20779 |
| RIG 4 | 20780 |

Add the required rigs under **Configuration → Rigs** before testing, then save. For self-hosted Docker, publish the same UDP ports on the container.

## Test the connection

1. Confirm **Listener · On** on the rig card.
2. Enter a driver name and select **Ready** before the first starting light.
3. Start a three-lap Grand Prix in the game.
4. Confirm **Collecting** and changing lap, lap time, speed and gear.
5. Open **Collector health → Rigs** and confirm packet counts increase.
6. Leave the game running through the results screen, then check the saved result and your destination dashboards.

A practice session can confirm that game data reaches the collector, but only a complete race tests capture and the saved result.

{{< callout type="default" >}}

**Use the displayed address**

A cloud address can change when an instance is replaced. Check it during event setup.

{{< /callout >}}

{{% /steps %}}

## If data does not appear

- Recheck the IP address and assigned port.
- Confirm the collector host firewall allows inbound UDP.
- Confirm the Docker or cloud port mapping exists.
- Make sure UDP Broadcast Mode is Off.
- Confirm the rig is configured and its listener is on.
- Use [Monitoring and Troubleshooting](/f1-2025/monitoring/) to separate UDP and destination problems.
