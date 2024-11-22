# Running the F1 2023 container

## Docker

The following Docker command will run the F1 2023 container (support for `amd/64` and `arm/64` architectures) and expose the required ports for the UI and UDP listener(s):

```bash
docker run --name f1_2024 -d \
-p 8501:8501/tcp \
-p 20777:20777/udp \
ghcr.io/splunk/f1_2024:latest
```

The above will run the F1 2023 container in the background and expose port `8501` for the UI and port `20777` for the UDP listener.

!!! note

If you are using more than one simulator you can expose up to **8 UDP** ports, for example, if you have 4 simulators running you would start the container by running:

```bash
docker run --name f1_2024 -d \
-p 8501:8501/tcp \
-p 20777:20777/udp \
-p 20778:20778/udp \
-p 20779:20779/udp \
-p 20780:20780/udp \
ghcr.io/splunk/f1_2024:latest
```

## Validation

To validate the container is running correctly you can run the following command:

=== "Command"

    ``` bash
    docker port f1_2024
    ```

=== "Output"

    ``` bash
    8501/tcp -> 0.0.0.0:8501
    20777/udp -> 0.0.0.0:20777
    ```
