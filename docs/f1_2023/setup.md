# Running the F1 2023 container

For both Mac OS and Ubuntu the following Docker command will run the F1 2023 container:

```bash
docker run --name f1_2023 -d -p 8501:8501/tcp -p 20777:20777/udp rcastley895/f1_2023
```

The above will run the F1 2023 container in the background and expose port `8501` for the UI and port `20777` for the UDP listener.

!!! note

    If you are using more than one simulator you can expose up to 8 UDP ports, for example, if you have 4 simulators running you would start the container by running:

    ```bash
    docker run --name f1_2023 -d -p 8501:8501/tcp -p 20777:20777/udp -p 20778:20778/udp -p 20779:20779/udp -p 20780:20780/udp rcastley895/f1_2023
    ```

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
