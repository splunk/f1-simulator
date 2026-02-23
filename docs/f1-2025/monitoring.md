# Monitoring System Health

This guide covers monitoring the F1 2025 Data Collector's health, verifying data flow, and troubleshooting common issues.

## Status Bar

The status bar at the top of the Collector page provides at-a-glance system health via LED indicators.

### Master Control

Located on the left side of the status bar.

- **SYSTEMS LIVE** (green pulsing LED) — All collectors running
- **SYSTEMS OFFLINE** (muted) — Collectors stopped
- **DEPLOYING...** — Configuration change in progress

### External IP

A blue LED badge displays the collector's external IP address. Use this IP in the F1 game's telemetry settings.

### Redis Connection Status

- 🟢 **Green** — Redis database connected and operational
- 🔴 **Red** — Redis connection failed or unavailable

**What Redis Does:**

- Stores driver names
- Caches configuration settings
- Tracks race completion status

**If Redis is Down:**

- Collectors will continue to work
- Driver names may not persist
- Race completion tracking may not function
- Configuration changes may not save

**Troubleshooting Red Redis Status:**

```bash
# Check if Redis container is running
docker ps | grep redis

# Restart the container
docker restart f1-2025

# Check container logs
docker logs f1-2025
```

### Collectors Status

Shows how many collectors are currently running out of the total configured.

**Display Format:** `X/Y Collectors`

- **X** = Number of active collectors
- **Y** = Total number of configured collectors

**LED Colour:**

- 🟢 **Green** — All collectors running (X = Y)
- 🟠 **Amber** — Some collectors running (X < Y)
- ⚫ **Off** — No collectors running (X = 0)

## Rig Card Indicators

Each rig card displays status pills and live metrics for detailed per-rig monitoring.

### Endpoint Status

When Observability Cloud or HEC destinations are enabled, each rig card shows endpoint health pills:

- **O11y ✓** / **HEC ✓** (green) — Data successfully sent to endpoint
- **O11y ✗** / **HEC ✗** (red) — Endpoint unreachable or rejecting data
- **O11y —** / **HEC —** (muted) — No data sent yet (pending first transmission)

### Endpoint Failure Banner

If an endpoint fails, a red error banner appears at the top of the page with details about the failure. This helps identify configuration issues (wrong token, unreachable URL, etc.) immediately.

### Network Queue Status

Each rig card displays a queue health pill showing the state of outbound network requests:

| State | Colour | Meaning |
| ----- | ------ | ------- |
| **QUEUE OK** | Green | All requests flowing — no drops, inflight below 50% capacity |
| **Q:12/50** | Amber | Inflight requests ≥ 50% of max — backpressure building |
| **3 DROP** | Red | Requests are being dropped — Splunk endpoint may be unreachable or slow |

**Troubleshooting Queue Issues:**

- **Amber (backpressure)** — Temporary network slowness. Usually resolves on its own. Check endpoint health.
- **Red (drops)** — Verify Splunk endpoint is reachable. Check HEC URL and tokens. May indicate network or firewall issues.

### UDP Port Status

Each rig card displays the UDP port number with colour coding:

- 🟢 **Green** — Collector running and ready to receive telemetry
- ⚫ **Muted** — Collector not running

### Race Complete Flag

A flag icon with **RACE COMPLETE** appears as a green pill when the race session has ended (after receiving `FinalClassificationData`). This unlocks the driver name for editing.

## Real-time Data Verification

When collectors are running and receiving data from F1 2025, live metrics appear on each rig card.

### Speed

- **Display:** Current vehicle speed in mph
- **Updates:** Continuously during gameplay
- **Expected Behaviour:**
    - 0 mph when stationary (pits, menus)
    - Fluctuating values during racing
    - Max speeds vary by track (Monaco ~180 mph, Monza ~220 mph)

**Troubleshooting:**

- No speed shown = no telemetry data being received
- Speed stuck at 0 = driver may be in menu/paused
- Speed frozen = possible network issue or game frozen

### Current Lap

- **Display:** Live lap counter
- **Updates:** Increments as driver completes laps
- **Expected Behaviour:**
    - Lap 0 during warm-up/out lap
    - Lap 1 after crossing start/finish line
    - Increments each lap thereafter

**Troubleshooting:**

- Lap not incrementing = driver may not be in race session
- Lap counter missing = no telemetry data

### Track

- **Display:** Current track name
- **Examples:** "Silverstone", "Monaco", "Spa-Francorchamps", "Suzuka"
- **Updates:** When track loads in game

**Troubleshooting:**

- No track name = telemetry not being received
- Wrong track name = data from different session/rig

## System Health Checklist

Use this checklist to verify system health before and during events.

### Pre-Event Health Check

- [ ] Redis status shows green in status bar
- [ ] Configuration deployed with correct credentials
- [ ] Driver names set for all active rigs
- [ ] Master Control toggled to SYSTEMS LIVE
- [ ] Collectors status shows `X/X` (all running) in green

### During Event Health Check

- [ ] All active rig UDP ports are green
- [ ] Real-time speed values updating
- [ ] Lap counters incrementing as races progress
- [ ] Track names displaying correctly
- [ ] O11y/HEC endpoint pills showing ✓
- [ ] Queue status showing QUEUE OK
- [ ] Memory usage within normal range (50-200 MB per collector)

### Post-Event Health Check

- [ ] RACE COMPLETE status appeared for all completed races
- [ ] All data visible in Splunk dashboards
- [ ] No endpoint failure banners displayed
- [ ] Collectors stopped cleanly when Master Control toggled off

## Monitoring Best Practices

### Keep Interface Visible

- Display the Collector page on a monitor during events
- Allows quick identification of issues
- Real-time verification that data is flowing

### Watch the Status Pills

- Endpoint pills (O11y/HEC) are the most critical indicators
- Green ✓ = data flowing to Splunk
- Red ✗ = immediate attention needed
- Queue drops = network or endpoint issue

### Monitor Memory Usage

**Normal Memory Usage:**

- 50-150 MB per collector (typical)
- 150-200 MB per collector (high load)
- Total system memory should be <1 GB for 4 collectors

**High Memory Usage:**

- \>300 MB per collector = potential issue
- May indicate data buildup or network problems
- Consider restarting collectors

**How to Check:**

- Memory usage displayed as an amber pill on each rig card
- Can also check container stats:

```bash
docker stats f1-2025
```

### Regular Status Checks

During long events, check status every 15-30 minutes:

- All endpoint pills green?
- Queue status OK?
- Real-time data still updating?
- Memory usage normal?
- Any error banners?

## Troubleshooting Guide

### UDP Port Not Receiving Data

**Problem:** Collector running but no telemetry data appears.

**Possible Causes & Solutions:**

1. **F1 2025 not running on rig**
   - Start the game
   - Verify telemetry is enabled in game settings

2. **Wrong IP address in game telemetry settings**
   - Check External IP in the status bar (blue badge)
   - Update game telemetry settings with correct IP

3. **Network connectivity issue**
   - Ping controller IP from rig PC
   - Check firewall rules
   - Verify UDP port not blocked

4. **Wrong UDP port configured**
   - Verify game is sending to correct port (20777, 20778, etc.)
   - Each rig needs unique port number

5. **Game in menu/paused**
   - Driver must be in session (practice, qualifying, race)
   - Telemetry doesn't stream from menus

**Verification Steps:**

```bash
# From the rig PC, test network connectivity
ping <controller-ip>

# Check if UDP port is accessible (requires netcat)
nc -u <controller-ip> 20777
```

### Endpoint Status Shows ✗

**Problem:** O11y or HEC pill is red.

**Possible Causes & Solutions:**

1. **Invalid token**
   - Open Config panel and verify credentials
   - Re-enter the token and deploy configuration

2. **Incorrect URL**
   - Verify HEC URL format: `https://<instance>:8088`
   - Must use HTTPS (not HTTP)

3. **Firewall blocking connection**
   - Test connectivity to endpoint
   - Check network/firewall rules

4. **Endpoint not enabled**
   - Open Config panel and verify the toggle is on

**Test HEC connectivity:**

```bash
curl -k https://<splunk-hec-url>:8088/services/collector \
  -H "Authorization: Splunk <hec-token>" \
  -d '{"event": "test"}'
```

### Queue Showing Drops

**Problem:** Queue pill shows red with drop count.

**Possible Causes:**

- Splunk endpoint temporarily unavailable
- Network latency or packet loss
- HEC endpoint overloaded

**Solutions:**

1. Check endpoint status pills — if also red, fix the endpoint issue first
2. Verify network connectivity to Splunk
3. Restart collectors (toggle Master Control off then on)

### Collector Shows Stopped

**Problem:** Rig card not showing as running.

**Possible Causes & Solutions:**

1. **Master Control is off**
   - Toggle Master Control to SYSTEMS LIVE

2. **Collector crashed**
   - Check logs for errors
   - Restart collectors (toggle Master Control off then on)

3. **Configuration issue**
   - Verify configuration is deployed
   - Check that the correct number of rigs is configured

### Redis Status is Red

**Problem:** Redis LED shows red in status bar.

**Impact:**

- Driver names may not save
- Configuration changes may not persist
- Race completion tracking disabled

**Solutions:**

1. **Restart the container:**

   ```bash
   docker restart f1-2025
   ```

2. **Check container logs:**

   ```bash
   docker logs f1-2025
   ```

### High Memory Usage

**Problem:** Container memory usage >300 MB or climbing continuously.

**Possible Causes:**

- Network issues causing data backup
- Too many simultaneous connections
- Memory leak (rare)

**Solutions:**

1. **Monitor over time** — Is it stable or growing?

2. **Restart collectors:**
   - Toggle Master Control off
   - Wait 10 seconds
   - Toggle Master Control on

3. **Restart entire container:**

   ```bash
   docker restart f1-2025
   ```

## Log Files

The collector generates detailed logs for troubleshooting.

### Accessing Logs

**Via the UI:**

The Collector page has a built-in log viewer accessible via the API.

**Via Docker:**

```bash
docker logs f1-2025
```

**Via API:**

```bash
# JSON format (default)
curl http://localhost:8501/api/logs

# Plain text format
curl "http://localhost:8501/api/logs?format=text"

# Last 20 lines
curl "http://localhost:8501/api/logs?format=text&lines=20"
```

## Help Panel

Click the **?** button in the top-right of the navigation bar to open the Help panel. It provides a quick reference for rig card indicators, queue states, and configuration options.

## Next Steps

- **[Manage Collectors](managing-collectors.md)** - Start/stop collectors and manage driver names
- **[Controller Configuration](controller-config.md)** - Configure Splunk destinations
- **[View Dashboards](dashboards.md)** - Access your data in Splunk
