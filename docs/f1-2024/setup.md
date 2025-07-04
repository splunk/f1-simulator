# Running the F1 2024 container

## Docker

Create a startup script (`start.sh`) to run the F1 2024 container (support for `amd/64` and `arm/64` architectures) and expose the required ports for the UI and UDP listener(s):

```bash
#!/bin/bash
if [[ ! -e ~/players.sqlite ]]; then
    touch ~/players.sqlite
fi

docker run -d \
-v ~/players.sqlite:/app/players.sqlite \
--name f1-2024 \
--restart always \
-p 8501:8501/tcp \
-p 20777:20777/udp \
-p 20777:20778/udp \
-p 20777:20779/udp \
-p 20777:20780/udp \
ghcr.io/splunk/f1-2024:latest
```

The above will run the F1 2024 container in the background and expose port `8501` for the UI and ports`20777-27780` for the UDP listener.

## Validation

To validate the container is running correctly you can run the following command:

=== "Command"

    ```bash
    docker port f1-2024
    ```

=== "Output"

    ```bash
    8501/tcp -> 0.0.0.0:8501
    20777/udp -> 0.0.0.0:20777
    ```
