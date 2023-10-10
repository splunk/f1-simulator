# Pre-requisites

## Recommended environment(s)

- Apple MacBook (Apple Silicon M1/M2)
- AWS/EC2 (Ubuntu 22.04 or above)
    - t2.large (2 vCPU, 8GB RAM)
    - External IP address
    - Inbound access on ports `8501/tcp` and `20777-20784/udp`

## Install Docker

Docker is required to run the F1 2023 UDP listener and UI. The UDP listener will take the UDP stream from F1 2023 and transform the stream into metric payload for Splunk Observability Cloud and Splunk Enterprise/Cloud. The UI is used to configure where to send the metrics, start/stop the UDP listener(s) and change the name of the current driver.

The following instructions will install Docker on your laptop or EC2 instance:

=== "Mac OS"
  
    [Download Docker Desktop for Mac with Apple Silicon](https://desktop.docker.com/mac/main/arm64/Docker.dmg?utm_source=docker&utm_medium=webreferral&utm_campaign=docs-driven-download-mac-arm64)

=== "Ubuntu"

    ```bash
    sudo apt remove docker docker-engine docker.io containerd runc
    sudo apt update
    sudo apt install ca-certificates curl gnupg -y
    sudo install -m 0755 -d /etc/apt/keyrings
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
    sudo chmod a+r /etc/apt/keyrings/docker.gpg
    echo \
    "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
    "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
    sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    sudo apt update
    sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin -y
    sudo usermod -aG docker $USER
    ```
