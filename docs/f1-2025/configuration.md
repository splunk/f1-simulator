# Using the F1 2025 Collector

The F1 2025 Data Collector provides a web-based interface for configuring, managing, and monitoring real-time telemetry collection from F1 racing simulators.

## Getting Started

Follow these guides in order to set up and run your F1 2025 data collection:

### 1. Controller Configuration

Configure your event settings and Splunk destinations.

**[→ Controller Configuration Guide](controller-config.md)**

### 2. F1 2025 Game Setup

Configure UDP telemetry in the F1 2025 game on each racing rig.

**[→ Game Telemetry Configuration](telemetry.md)**

### 3. Managing Collectors

Start, stop, and manage data collection for your event.

**[→ Managing Collectors Guide](managing-collectors.md)**

### Key Status Indicators

| Indicator | Colour/Status | Colour/Status | Meaning |
|-----------|-------|------------|---------|
| UDP Port | 🟢 | ⚪ | Receiving telemetry data |
| Collection Status | **RUNNING** | **STOPPED** | Collector active/inactive |
| Redis | ✓ | ✗ | Database connected |
| Collectors | All Collectors running | Some/No Collectors running | Collector health |

Start with the [Controller Configuration](controller-config.md) guide to set up your event.
