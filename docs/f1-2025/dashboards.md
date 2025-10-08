# Viewing Your Data in Dashboards

Once your F1 2025 collector is streaming telemetry data, you can visualize and analyze it using pre-built dashboards in Splunk Observability Cloud and Splunk Enterprise/Cloud.

## Splunk Observability Cloud

### Dashboard Group

A pre-built dashboard group is available for Splunk Observability Cloud that provides real-time visualization of F1 telemetry data.

### Importing the Dashboard

1.  **Download the dashboard JSON file:** [Download F1 2025 Dashboard Group](https://github.com/splunk/f1-simulator/blob/main/observability/dashboard_group_F1_2025.json)

2.  **Import into Observability Cloud:**
    1. Navigate to **Dashboards** in Splunk Observability Cloud
    2. Click **Create** → **Import**
    3. Upload the downloaded JSON file
    4. Click **Import**

3.  **Access the dashboards:**
    1. Navigate to **Dashboards**
    2. Find the **F1 2025** dashboard group

## Splunk Enterprise/Cloud

### Data Drivers App

The DataDrivers App provides comprehensive dashboards for analyzing F1 telemetry data in Splunk Enterprise and Splunk Cloud.

#### Installation Methods

Choose the installation method that works best for your environment.

=== "Manual Installation"

    Install the app manually by uploading the package file.

    ##### Clone the DataDrivers App repository:

    ```bash
    git clone https://github.com/splunk/datadrivers-app.git
    ```

    ##### Create a tar.gz package:

    ```bash
    tar --disable-copyfile --exclude='.*' --exclude='._*' -cvzf datadrivers-app.tar.gz datadrivers-app
    ```

    ##### Upload to Splunk:
    - Navigate to **Apps** → **Manage Apps** in your Splunk instance
    - Click **Install app from file**
    - Browse for the `datadrivers-app.tar.gz` file
    - Click **Upload**

=== "Remote Installation"

    For managed Splunk environments, install the app via deployment server for automatic updates.


    ##### Configure the deployment client:

    Edit `/opt/splunk/etc/system/local/deploymentclient.conf`:

    ```ini
    [target-broker:deploymentServer]
    targetUri = https://dddemo.notsplunktshirtco.com:8089

    [deployment-client]
    phoneHomeIntervalInSecs = 60
    ```

    ##### Restart Splunk:

    ```bash
    sudo /opt/splunk/bin/splunk restart
    ```

    ##### Wait for deployment:
    1. After Splunk restarts, it will contact the deployment server
    2. The Data Drivers App will be downloaded and installed automatically
    3. Splunk will restart again to load the app
    4. Any future updates will be applied automatically

    ##### Benefits of Deployment Server Method:

    - Automatic updates to dashboards
    - Centralized management
    - Consistent deployment across multiple Splunk instances
    - Automatic bug fixes and improvements

### Accessing the Dashboards

After installation:

1. Navigate to **Apps** in your Splunk instance
2. Click **Data Drivers - F1 2025**
3. Select a dashboard from the navigation menu
