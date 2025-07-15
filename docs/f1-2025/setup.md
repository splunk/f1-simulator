# Running the F1 2025 container

## Docker

Create a startup script (`start.sh`) to run the F1 2025 container (support for `amd/64` and `arm/64` architectures) and expose the required ports for the UI and UDP listener(s):

```bash
#!/bin/bash
if [[ ! -e ~/players.sqlite ]]; then
    touch ~/players.sqlite
fi

docker run -d \
-v ~/players.sqlite:/app/players.sqlite \
--name f1-2025 \
--restart always \
-p 8501:8501/tcp \
-p 20777:20777/udp \
-p 20778:20778/udp \
-p 20779:20779/udp \
-p 20780:20780/udp \
ghcr.io/splunk/f1-2025:latest
```

The above will run the F1 2025 container in the background and expose port `8501` for the UI and ports`20777-27780` for the UDP listener.

## Validation

To validate the container is running correctly you can run the following command:

=== "Command"

    ```bash
    docker port f1-2025
    ```

=== "Output"

    ```text
    8501/tcp -> 0.0.0.0:8501
    20777/udp -> 0.0.0.0:20777
    20778/udp -> 0.0.0.0:20778
    20779/udp -> 0.0.0.0:20779
    20780/udp -> 0.0.0.0:20780
    ```
