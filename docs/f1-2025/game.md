# F1 2025 Telemetry Configuration

In the F1 2025 game you will need to configure the telemetry settings to send data to the F1 2025 collector.

* On the main screen select **Game Options**, then click on **Settings** and then **Telemetry Settings**.

    <pre>
    UDP Telemetry: **On**
    UDP Broadcast Mode: **Off**
    UDP IP Address: **IP address of the laptop/EC2 instance running the container**
    UDP Port: **20777**
    UDP Send Rate: **10Hz**
    UDP Format: **2025**
    Your Telemetry: **Restricted**
    Show Online IDs: **Off**
    </pre>

If you are running multiple simulators, you will need to repeat the above for each remembering to change the UDP Port for each simulator.

![Telemetry Settings](../assets/screenshots/telemetry.png)
