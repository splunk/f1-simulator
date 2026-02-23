# Managing Data Collectors

This guide covers starting, stopping, and managing the F1 2025 data collectors.

## Master Control

The Master Control toggle in the top-left of the status bar provides centralized control over all data collectors.

### Starting All Collectors

1. Click the **Master Control** toggle in the status bar
2. The status changes to **SYSTEMS LIVE** with a pulsing green LED
3. All configured collectors start simultaneously

**What Happens:**

- Collectors for all configured rigs start listening for UDP telemetry
- UDP ports open and begin accepting data
- Data flows to configured Splunk destinations
- Rig card status pills update to reflect running state

### Stopping All Collectors

1. Click the **Master Control** toggle to switch off
2. The status changes to **SYSTEMS OFFLINE**

**What Happens:**

- All collectors stop processing data
- UDP ports stop listening
- No data is sent to Splunk destinations
- Rig card status pills update accordingly

!!! tip "Use Master Control for Events"
    Master Control is ideal for coordinated start/stop during events. All rigs begin and end data collection simultaneously.

## Rig Cards

Each configured rig is displayed as a card in the main area. Cards are arranged in a responsive grid — single column for 1-2 rigs, two columns for 3-4 rigs.

### Status Pills

Each rig card displays a row of status pills at the top:

| Pill | Description |
| ---- | ----------- |
| **Rig ID** (blue) | Rig identifier (e.g. `RIG 1`, `RIG 2`) |
| **UDP port** | Listening port number — green when running, muted when stopped |
| **Memory** (amber) | Collector process memory usage in MB (visible when running) |
| **O11y** | Observability Cloud endpoint status — ✓ (green), ✗ (red), or — (pending). Only shown when O11y is enabled |
| **HEC** | Splunk HEC endpoint status — ✓ (green), ✗ (red), or — (pending). Only shown when HEC is enabled |
| **Queue** | Network queue health — see [Monitoring](monitoring.md) for details |
| **Race Complete** | Appears with a flag icon when a race has finished |

### Live Metrics

When a rig is running and receiving telemetry data, three hero metrics appear:

- **Speed MPH** — Current vehicle speed
- **Lap** — Live lap counter
- **Track** — Current track name (e.g. "Silverstone", "Monaco", "Spa")

If a collector is running but no telemetry data has been received yet, the card displays "Awaiting telemetry data..."

## Driver Management

Each rig has an associated driver name displayed at the bottom of the card. This name is used as a dimension in telemetry data and appears in Splunk dashboards.

### Editing Driver Names

1. **Click** the driver name area on the rig card — the row highlights on hover with an edit icon
2. The name field becomes an inline text input
3. Type the new driver name
4. Press ++enter++ or click **Save** to confirm
5. Press ++escape++ or click **✕** to cancel

### Race Completion Rule

!!! warning "CRITICAL: Driver Name Update Restriction"
    Driver names can **only** be updated when the rig displays the **RACE COMPLETE** status pill.

**Why This Restriction Exists:**

- Prevents data corruption during active races
- Ensures all lap data is correctly attributed to the same driver
- Maintains data integrity in Splunk dashboards

**How It Works:**

1. Driver starts a race — driver name is locked
2. Driver completes the race — system receives `FinalClassificationData` packet
3. Rig card displays **RACE COMPLETE** status pill
4. Driver name becomes editable
5. Update driver name for the next driver
6. New race starts — driver name locks again

**Best Practice for Multi-Driver Events:**

- Wait for **RACE COMPLETE** before swapping drivers
- Update the driver name immediately after race completion
- Have the next driver ready to start their session

!!! danger "Do Not Update Driver Name Mid-Race"
    Never update a driver name while a race is in progress. This will corrupt the data attribution in Splunk.

## Next Steps

- **[Configure F1 2025 Game](telemetry.md)** - Set up game telemetry settings
- **[View Dashboards](dashboards.md)** - Access your data in Splunk
