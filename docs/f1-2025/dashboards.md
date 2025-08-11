# Dashboards

## Splunk Observability Cloud

You can import the following dashboard group into your Observability Cloud Organization.

Download the JSON file [**here**](https://github.com/splunk/f1-simulator/blob/main/observability/dashboard_group_F1_2025.json).

## Splunk Enterprise/Cloud

The source code for the Splunk dashboards is available in the [DataDrivers App Repository](https://github.com/splunk/datadrivers-app). You can install the app using the following instructions:

1. Check out the [DataDrivers App Repository](https://github.com/splunk/datadrivers-app)
2. Create a `tar.gz`:

    ```bash
    tar --disable-copyfile --exclude='.*' --exclude='._*' -cvzf datadrivers-app.tar.gz datadrivers-app
    ```

3. Goto **Apps** > **Manage Apps** in your Splunk Enterprise/Cloud instance and click on **Install app from file**.
4. Browse for the `datadrivers-app.tar.gz` file and click **Upload**.
5. Once the app is installed, you can access the dashboards by navigating to **Apps** > **DataDrivers F1 Racing**.
