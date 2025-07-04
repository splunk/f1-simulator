# F1 2025 Telemetry Configuration

In the F1 2025 you will need to configure the telemetry settings to send data to the F1 2025 container.

On the main screen select **Game Options**, then click on **Settings** and then **Telemetry Settings**.

Here you will need to set the following:

* UDP Telemetry: **On**
* UDP Broadcast Mode: **Off**
* UDP IP Address: **IP address of the laptop/EC2 instance running the container**
* UDP Port: **20777**
* UDP Send Rate: **10Hz**
* UDP Format: **2025**

If you are running multiple simulators, you will need to repeat the above for each remebering to change the UDP Port for each simulator.

![F1 2024 Telemetry Settings](../assets/screenshots/f1_2023_telemetry_settings.png)
