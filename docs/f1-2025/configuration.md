# F1 2025 Data Collector - User Guide

## Overview

The F1 2025 Data Collector is a comprehensive telemetry collection system that captures real-time F1 game data and sends it to Splunk platforms for analysis and visualization. The system consists of a web-based control interface and background data collectors that capture UDP telemetry from F1 2025.

## Getting Started

### 1. Initial Configuration

1. **Set Collection Parameters**
   - **Rigs**: Choose the number of F1 rigs to monitor (1-4)
   - **Event Name**: Enter a custom event name for dashboard identification

2. **Launch the Application**
   - Run the main application to access the web interface
   - The interface will display the F1 2025 Data Drivers dashboard

3. **Configure Data Destinations**
   Use the Configuration panel in the sidebar to set up your data endpoints:

   **Observability Cloud Settings:**

   - Select your Splunk Observability Cloud realm (eu0, eu1, eu2, us0, us1, us2, au0, jp0, sg0)
   - Enter your Access Token (this will be masked for security)
   - Check "Enable Observability Cloud" to activate metric collection

   **Splunk Enterprise Settings:**

   - Enter your HEC URL and port (e.g., `https://your-splunk.com:8088`)
   - Enter your HEC Token (this will be masked for security)
   - Check "Enable Splunk Cloud" to activate event collection

4. **Set Collection Parameters**
   - **Playback Mode**: Select "False" for live F1 games, "True" for demo/testing

5. **Save Configuration**
   - Click "Save Configuration" to apply your settings
   - The system will create the necessary database tables and initialize the collectors

### 2. Managing Data Collection

#### Master Control

Use the **Master Control** toggle to start/stop all data collectors simultaneously:

- **ON**: Starts collectors for all configured rigs
- **OFF**: Stops all running collectors

#### Individual Rig Status

Each rig displays comprehensive status information:

- **Rig Identifier**: Shows the rig hostname (e.g., RIG_1)
- **UDP Port**: Displays the listening port number with connection status
- **Collection Status**: Shows RUNNING (green) or STOPPED (red)
- **Race Complete Flag**: Indicates when a race has finished
- **Real-time Metrics**: When running, displays current speed, lap number, and track information

### 3. Player Management

#### Setting Player Names

Each rig has a player name field that can be updated:

1. **Enter Player Name**: Type the driver's name in the text field
2. **Update**: Click the "Update" button to save the change

#### Important Race Completion Rule

🚨 **CRITICAL**: Player names can only be updated when the UI displays **RACE COMPLETE** for that rig.

- The system tracks race completion status automatically
- When a race finishes (FinalClassificationData packet received), the rig shows **RACE COMPLETE**
- Only then can you update the player name for the next driver
- This prevents data corruption during active races

### 4. Monitoring System Health

#### Connection Status Indicators

The sidebar displays system health information:

- **Redis Badge**:
  - Green ✓ = Redis database connected
  - Red ✗ = Redis connection failed

- **Collectors Status**:
  - Shows "X/Y collectors running" (X active out of Y total)
  - Green = All collectors running
  - Orange = Some or no collectors running

#### Real-time Data Verification

When collectors are running and receiving data:

- **Speed**: Current vehicle speed in mph
- **Current Lap**: Live lap counter
- **Track**: Current track name (e.g., "Silverstone", "Monaco")

### 5. Best Practices

#### Event Management

- Set meaningful Event Names for easy identification in Splunk dashboards
- Use consistent naming conventions across multiple events

#### Performance Optimization

- Monitor system resources when running multiple collectors
- Consider network bandwidth when sending to multiple Splunk endpoints

#### Race Operations

- Always wait for "RACE COMPLETE" status before changing drivers
- Use the Master Control for coordinated start/stop of all collectors
- Monitor real-time metrics to verify data collection during races

## Support and Maintenance

### Log Files

The system generates log files (`collector.log`) containing:

- Collector startup and shutdown events
- Data transmission statistics
- Error messages and debugging information
