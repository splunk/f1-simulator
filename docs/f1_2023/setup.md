# Running the F1 2023 container

## Mac OS

The following Docker command will run the F1 2023 container on Mac OS:

```bash
docker run --name f1_2023 -d -p 8501:8501/tcp -p 20777:20777/udp ghcr.io/splunk/f1_2023:latest
```

The above will run the F1 2023 container in the background and expose port `8501` for the UI and port `20777` for the UDP listener.

!!! note

    If you are using more than one simulator you can expose up to 8 UDP ports, for example, if you have 4 simulators running you would start the container by running:

    ```bash
    docker run --name f1_2023 -d -p 8501:8501/tcp -p 20777:20777/udp -p 20778:20778/udp -p 20779:20779/udp -p 20780:20780/udp ghcr.io/splunk/f1_2023:latest
    ```

## Ubuntu

The following Docker command will run the F1 2023 container on Ubuntu:

```bash
docker run --name f1_2023 -d -p 8501:8501/tcp -p 20777:20777/udp ghcr.io/splunk/f1_2023-amd64:latest
```

The same instructions to expose additional UDP ports apply to Ubuntu as well as was described in the Mac OS section.

## Validation

To validate the container is running correctly you can run the following command:

=== "Command"

    ```bash
    docker port f1_2023
    ```

=== "Output"

    ```bash
    8501/tcp -> 0.0.0.0:8501
    20777/udp -> 0.0.0.0:20777
    ```
