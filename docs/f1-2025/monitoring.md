# Monitoring System Health

This guide covers monitoring the F1 2025 Data Collector's health, verifying data flow, and troubleshooting common issues.

## Status Indicators

The controller interface provides multiple status indicators to monitor system health.

### Redis Connection Status

Located in the sidebar, the Redis badge shows the database connection status.

**Indicators:**

- 🟢 **Green ✓** - Redis database connected and operational
- 🔴 **Red ✗** - Redis connection failed or unavailable

**What Redis Does:**

- Stores player/driver names
- Caches configuration settings
- Tracks race completion status

**If Redis is Down:**

- Collector will continue to work
- Player names may not persist
- Race completion tracking may not function
- Configuration changes may not save

**Troubleshooting Red Redis Status:**

```bash
# Check if Redis container is running
docker ps | grep redis

# Restart Redis container (if using Docker Compose)
docker-compose restart redis

# Check Redis logs
docker logs <redis-container-name>
```

### Collectors Status

Shows how many collectors are currently running out of the total configured.

**Display Format:** `X/Y collectors running`

- **X** = Number of active collectors
- **Y** = Total number of configured collectors

**Color Coding:**

- 🟢 **Green** - All collectors running (X = Y)
- 🟠 **Orange** - Some or no collectors running (X < Y)

**Examples:**

- `4/4 collectors running` (Green) - All good, all rigs active
- `2/4 collectors running` (Orange) - Only 2 out of 4 configured rigs are running
- `0/4 collectors running` (Orange) - Master Control is OFF or all collectors stopped

### UDP Port Status

Each rig displays a UDP port indicator showing whether data is being received.

**Indicators:**

- 🟢 **Green Port** - Actively receiving telemetry data from F1 2025
- 🔴 **Red Port** - Not receiving data (no connection)

**What This Tells You:**

- Green = F1 2025 game is sending telemetry to this collector
- Red = Game is not sending data, or network issue exists

## Real-time Data Verification

When collectors are running and receiving data from F1 2025, real-time metrics appear in the interface.

### Speed

- **Display:** Current vehicle speed in mph
- **Updates:** Continuously during gameplay
- **Expected Behavior:**
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
- **Expected Behavior:**
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

### Data Flow Status

- **RUNNING (Green):** Collector is active and processing data
- **STOPPED (Red):** Collector is not running

## System Health Checklist

Use this checklist to verify system health before and during events.

### Pre-Event Health Check

- [ ] Redis status shows green ✓
- [ ] Collectors status shows `X/X` (all running) in green
- [ ] All UDP ports configured for active rigs
- [ ] Configuration saved successfully
- [ ] Player names set for all active rigs

### During Event Health Check

- [ ] All active rig UDP ports are green
- [ ] Real-time speed values updating
- [ ] Lap counters incrementing as races progress
- [ ] Track names displaying correctly
- [ ] RUNNING status for all active collectors
- [ ] Memory usage within normal range (50-200 MB per collector)

### Post-Event Health Check

- [ ] RACE COMPLETE status appeared for all completed races
- [ ] All data visible in Splunk dashboards
- [ ] No error messages in logs
- [ ] Collectors stopped cleanly when Master Control disabled

## Monitoring Best Practices

### Keep Interface Visible

- Display the controller interface on a monitor during events
- Allows quick identification of issues
- Real-time verification that data is flowing

### Watch the UDP Ports

- UDP port status is the most critical indicator
- Green ports = data flowing
- Red ports = immediate attention needed

### Monitor Memory Usage

**Normal Memory Usage:**

- 50-150 MB per collector (typical)
- 150-200 MB per collector (high load)
- Total system memory should be <1 GB for 4 collectors

**High Memory Usage:**

- \>300 MB per collector = potential issue
- May indicate data buildup or network problems
- Consider restarting affected collector

**How to Check:**

- Memory usage displayed per rig in interface
- Can also check container stats:

```bash
docker stats f1-2025
```

### Regular Status Checks

During long events, check status every 15-30 minutes:

- All ports still green?
- Real-time data still updating?
- Memory usage normal?
- Any error messages?

## Troubleshooting Guide

### UDP Port is Red

**Problem:** Port indicator is red, not receiving data.

**Possible Causes & Solutions:**

1. **F1 2025 not running on rig**
   - Start the game
   - Verify telemetry is enabled in game settings

2. **Wrong IP address in game telemetry settings**
   - Check External IP at bottom of controller
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

### No Real-time Data Showing

**Problem:** UDP port is green but no speed/lap/track data appears.

**Possible Causes & Solutions:**

1. **Driver not in active session**
   - Must be in practice, qualifying, or race
   - Must be on track (not in pits/menus)

2. **Race hasn't started**
   - Data appears once session begins
   - May take a few seconds to populate

3. **Display refresh issue**
   - Refresh browser page
   - Check if data appears after refresh

### Collector Shows STOPPED

**Problem:** Individual collector status shows STOPPED (red).

**Possible Causes & Solutions:**

1. **Master Control is OFF**
   - Toggle Master Control to ON

2. **Collector crashed**
   - Check logs for errors
   - Restart collector (toggle Master Control OFF then ON)

3. **Configuration issue**
   - Verify configuration is saved
   - Check that rig is enabled

### Redis Status is Red

**Problem:** Redis badge shows red ✗.

**Impact:**

- Player names may not save
- Configuration changes may not persist
- Race completion tracking disabled

**Solutions:**

1. **Check Redis container:**

   ```bash
   docker ps | grep redis
   ```

2. **Restart Redis:**

   ```bash
   docker restart <redis-container-name>
   ```

3. **Check Redis connectivity:**

   ```bash
   docker logs <redis-container-name>
   ```

### High Memory Usage

**Problem:** Container memory usage >300 MB or climbing continuously.

**Possible Causes:**

- Network issues causing data backup
- Too many simultaneous connections
- Memory leak (rare)

**Solutions:**

1. **Monitor over time** - Is it stable or growing?

2. **Restart collector:**
   - Toggle Master Control OFF
   - Wait 10 seconds
   - Toggle Master Control ON

3. **Restart entire container:**

   ```bash
   docker restart f1-2025
   ```

### Data Not Appearing in Splunk

**Problem:** Collectors running, data flowing, but nothing in Splunk dashboards.

**Possible Causes & Solutions:**

1. **HEC token invalid**
   - Verify HEC token in configuration
   - Test token using curl:

   ```bash
   curl -k https://<splunk-hec-url>:8088/services/collector \
     -H "Authorization: Splunk <hec-token>" \
     -d '{"event": "test"}'
   ```

2. **HEC URL incorrect**
   - Verify URL format: `https://<instance>:8088`
   - Must use HTTPS (not HTTP)
   - Port must be 8088

3. **Firewall blocking port 8088**
   - Test connectivity to HEC endpoint
   - Check network/firewall rules

4. **Splunk Cloud/O11y not enabled**
   - Verify "Enable Splunk Cloud" is checked
   - Verify "Enable Observability Cloud" is checked (if using O11y)

5. **Data indexing delay**
   - Wait 1-2 minutes for data to appear
   - Refresh Splunk dashboard

**Enable Debug Mode** to see detailed transmission logs.

## Log Files

The collector generates detailed logs for troubleshooting.

### Accessing Logs

**Via Docker:**

```bash
docker logs f1-2025
```

**Log File Location:**

- Container: `/app/collector.log`
- Can be mounted as volume for persistent logs

### What Logs Contain

**Normal Operations:**

- Collector startup events
- Configuration loaded
- Data transmission statistics
- Collector shutdown events

**Errors:**

- Connection failures to Splunk/O11y
- UDP port binding errors
- Data parsing issues
- Network timeouts

**Debug Mode:**

- Detailed packet information
- Individual metric transmissions
- Timing information
- Stack traces for errors

### Reading Logs

**Successful startup:**

```
[INFO] F1 2025 Collector starting...
[INFO] Configuration loaded
[INFO] UDP listener started on port 20777
[INFO] Connected to Redis
[INFO] Connected to Splunk HEC
[INFO] Collector ready
```

**Data flowing:**

```
[INFO] Received telemetry packet from 192.168.1.100
[INFO] Speed: 180 mph, Lap: 5, Track: Silverstone
[INFO] Sent metrics to Splunk Observability Cloud
```

**Common errors:**

```
[ERROR] Failed to connect to HEC: Connection refused
[ERROR] Invalid HEC token
[ERROR] Redis connection failed
[ERROR] UDP port 20777 already in use
```

## Next Steps

- **[Manage Collectors](managing-collectors.md)** - Start/stop collectors and manage player names
- **[Controller Configuration](controller-config.md)** - Configure Splunk destinations
- **[View Dashboards](dashboards.md)** - Access your data in Splunk
