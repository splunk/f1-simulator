# Using the F1 2025 Collector

The F1 2025 Data Collector provides a web-based interface for configuring, managing, and monitoring real-time telemetry collection from F1 racing simulators.

## Interface Overview

The collector UI has three pages accessible via the navigation bar:

| Page | Description |
| ---- | ----------- |
| **Collector** | Main control page — Master Control, rig status cards, configuration |
| **Telemetry** | Live telemetry dashboard with charts and track map |
| **Pit Wall** | Pit wall overview of all active rigs |

A **Help** button (?) in the navigation bar opens a slide-over panel with a quick reference guide for the current page.

## Getting Started

Follow these guides in order to set up and run your F1 2025 data collection:

### 1. Controller Configuration

Open the Config panel to set up your event settings and Splunk destinations.

**[→ Controller Configuration Guide](controller-config.md)**

### 2. F1 2025 Game Setup

Configure UDP telemetry in the F1 2025 game on each racing rig.

**[→ Game Telemetry Configuration](telemetry.md)**

### 3. Managing Collectors

Start, stop, and manage data collection for your event.

**[→ Managing Collectors Guide](managing-collectors.md)**

### Key Status Indicators

| Indicator | Healthy | Unhealthy | Location |
| --------- | ------- | --------- | --------- |
| Master Control | SYSTEMS LIVE (green LED) | SYSTEMS OFFLINE | Status bar |
| Redis | Green LED | Red LED | Status bar |
| Collectors | X/X (green) | X/Y amber, 0/Y off | Status bar |
| UDP Port | Green (receiving data) | Muted (no data) | Rig card pill |
| O11y / HEC | ✓ (green) | ✗ (red) | Rig card pill |
| Queue | QUEUE OK (green) | DROP (red) | Rig card pill |

Start with the [Controller Configuration](controller-config.md) guide to set up your event.
