# F1 2025 Data Collector

The F1 2025 Data Collector captures real-time telemetry from F1 racing simulators and streams it to Splunk Enterprise and Splunk Observability Cloud for analysis and visualization.

## Choose Your Setup Path

### Option 1: Splunk Show

**Recommended for Events:** Pre-configured instance with Splunk Enterprise 10.0.0 and the collector already installed. Zero/minimal setup required.

To access the UI open a browser and navigate to `http://<show_instance>.splunk.show:81`, here you can configure where the game data is going to be sent.

**[→ Collector Configuration](configuration.md)**

### Option 2: Self-Hosted

Deploy the collector on your own laptop or cloud infrastructure using Docker.

**[→ Docker Setup Guide](docker-setup.md)**

## Need Help?

Reach out on Slack: [**#datadrivers-inh**](https://splunk.slack.com/archives/C03M3BSPLN7)
