# Managing Data Collectors

This guide covers starting, stopping, and managing the F1 2025 data collectors.

## Master Control

The Master Control toggle provides centralized control over all data collectors.

### Starting All Collectors

1. Locate the **Master Control** toggle at the top of the interface (orange toggle switch)
2. Click to switch to **ON** position
3. All configured collectors will start simultaneously

**What Happens:**

- Collectors for all configured rigs start listening for UDP telemetry
- UDP ports open and begin accepting data
- Data flows to configured Splunk destinations
- Status indicators update to show "RUNNING"

### Stopping All Collectors

1. Click the **Master Control** toggle to switch to **OFF** position
2. All running collectors stop immediately

**What Happens:**

- All collectors stop processing data
- UDP ports stop listening
- No data is sent to Splunk destinations
- Status indicators update to show "STOPPED"

!!! tip "Use Master Control for Events"
    Master Control is ideal for coordinated start/stop during events. All rigs begin and end data collection simultaneously.

## Individual Rig Status

Each rig displays comprehensive status information in the interface.

### Status Information Display

**Rig Identifier**

- Shows the rig hostname (e.g., `RIG_1`, `RIG_2`, `RIG_3`, `RIG_4`)
- Unique identifier for each racing simulator

**UDP Port**

- Displays the listening port number (e.g., `20777`, `20778`, `20779`, `20780`)
- Color-coded status indicator:
    - **Green:** Actively receiving data
    - **Grey:** No data being received

**Collection Status**

- **RUNNING** (green): Collector is active and processing data
- **STOPPED** (red): Collector is not running

**Container Memory Usage**

- Displays current memory usage in MB
- Helps monitor resource consumption
- Typical range: 50-100 MB per collector

**Race Complete Flag**

- Shows when a race has finished
- **RACE COMPLETE** indicator appears after final classification data received
- Important for player name changes (see below)

**Real-time Metrics** (when running)

- **Speed:** Current vehicle speed in mph
- **Current Lap:** Live lap counter
- **Track:** Current track name (e.g., "Silverstone", "Monaco", "Spa")

## Player Management

Each rig can have an associated player/driver name for identification in Splunk dashboards.

### Setting Player Names

1. Locate the player name field for the rig
2. Type the driver's name in the text field
3. Click the **"Update"** button

The player name will appear in Splunk dashboards and helps identify which driver's data you're viewing.

### Race Completion Rule

!!! warning "CRITICAL: Player Name Update Restriction"
    🚨 Player names can **only** be updated when the UI displays **RACE COMPLETE** for that rig.

**Why This Restriction Exists:**

- Prevents data corruption during active races
- Ensures all lap data is correctly attributed to the same driver
- Maintains data integrity in Splunk dashboards

**How It Works:**

1. Driver starts a race - player name is locked
2. Driver completes the race - system receives `FinalClassificationData` packet
3. UI displays **RACE COMPLETE** status
4. Player name field becomes editable
5. Update player name for the next driver
6. New race starts - player name locks again

**Best Practice for Multi-Driver Events:**

- Wait for **RACE COMPLETE** before swapping drivers
- Update the player name immediately after race completion
- Have the next driver ready to start their session
- Monitor the UI to confirm the new name is saved

!!! danger "Do Not Update Player Name Mid-Race"
    Never update a player name while a race is in progress. This will corrupt the data attribution in Splunk.

## Next Steps

- **[Configure F1 2025 Game](telemetry.md)** - Set up game telemetry settings
- **[View Dashboards](dashboards.md)** - Access your data in Splunk
