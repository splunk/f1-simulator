# Docker Setup for Self-Hosted Deployment

This guide covers setting up the F1 2025 collector using Docker on your local laptop or cloud instance.

!!! info "Using Splunk Show?"
    If you're using a Splunk Show instance, you don't need Docker setup. Go to the [Using the Collector](configuration.md) instead.

## Prerequisites

Choose your hosting platform:

=== "macOS (Laptop)"
    - Apple MacBook with Apple Silicon (M1/M2/M3)
    - Administrator access
    - Hardwired internet connection

    [**Download Docker Desktop for Mac with Apple Silicon**](https://desktop.docker.com/mac/main/arm64/Docker.dmg?utm_source=docker&utm_medium=webreferral&utm_campaign=docs-driven-download-mac-arm64)

    After installation:

    1. Open Docker Desktop
    2. Wait for Docker to start (whale icon in menu bar)
    3. Verify installation:

    ```bash
    docker --version
    ```

=== "Ubuntu (Cloud)"
    - AWS EC2 `t2.large` or equivalent
    - Ubuntu 22.04 or above
    - External IP address
    - Inbound access on ports `8501/tcp` and `20777-20784/udp`

    Run the following commands to install Docker on Ubuntu:

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
    sudo usermod -aG docker $USER    ```

    **Important:** Log out and log back in for group membership to take effect.

    Verify installation:

    ```bash
    docker --version
    ```

## Create Startup Script

Create a startup script (`start-collector.sh`) to run the F1 2025 container:

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

This script will:

- Create a SQLite database for player data (if it doesn't exist)
- Run the F1 2025 container in detached mode
- Mount the player database
- Expose port `8501` for the web UI
- Expose UDP ports `20777-20780` for telemetry (supports up to 4 rigs)
- Automatically restart the container if it stops

Make the script executable:

```bash
chmod +x start-collector.sh
```

Execute the startup script:

```bash
./start-collector.sh
```

Verify the container is running:

```bash
docker port f1-2025
```

Expected output:

```text
8501/tcp -> 0.0.0.0:8501
20777/udp -> 0.0.0.0:20777
20778/udp -> 0.0.0.0:20778
20779/udp -> 0.0.0.0:20779
20780/udp -> 0.0.0.0:20780
```

Check container status:

```bash
docker ps
```

You should see the `f1-2025` container running.

## AWS EC2 Security Group

Configure your security group to allow:

| Type | Protocol | Port Range | Source |
|------|----------|------------|--------|
| Custom TCP | TCP | 8501 | Your IP/CIDR |
| Custom UDP | UDP | 20777-20780 | Rig IPs/CIDR |

## Next Steps

Once your Docker container is running:

1. [Configure the Web Interface](configuration.md)
2. [Set up F1 2025 Game Telemetry](telemetry.md)
