# PREWORK - How To Get Data To Splunk Enterprise

Below is an overview of the data pipeline for a data drivers event.

1. In F1 2021, UDP telemetry output is controlled via the menus on all platforms. To enable it, from the Main menu enter the Game Options menu:

2. Enter the Settings menu

    ![x](RackMultipart20221106-1-vdo0mp_html_96017cff39a016b2.png)

3. Enter the Telemetry Settings menu

    ![x](RackMultipart20221106-1-vdo0mp_html_96057656df7eb5f.png)

4. Configure the Telemetry settings as such:
    1. UDP Telemetry: On
    2. UDP Broadcast Mode: Off
    3. UDP IP Address: IP Address of the Ethernet on the local laptop
    4. UDP Port: depends on the rig
        1. Sim\_rig\_1: 20777
        2. Sim\_rig\_2: 20778
        3. Sim\_rig\_3: 20779
        4. Sim\_rig\_4: 20780
    5. UDP Send Rate: 10Hz
    6. UDP Format: 2020
    7. Your Telemetry: Public

5. The game will start transmitting useful telemetry data only when you start driving a timed lap.
6. Escape back to Main Menu and continue with the style play that is relevant for you.

![x](RackMultipart20221106-1-vdo0mp_html_2b1b7d8ad315757d.png)
