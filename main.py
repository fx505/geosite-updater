#!/usr/bin/env python3
import os
import subprocess

def main():
    # Directory where assets will be stored
    assets_dir = "/var/lib/marzban/assets/"

    # Full paths to docker-compose and wget
    docker_compose_bin = "/usr/local/bin/docker-compose"
    wget_bin = "/usr/bin/wget"

    # Create the assets directory if it doesn't exist
    os.makedirs(assets_dir, exist_ok=True)

    # Download geosite.dat and geoip.dat
    subprocess.run([wget_bin, "-O", f"{assets_dir}geosite.dat", "https://github.com/chocolate4u/Iran-v2ray-rules/releases/latest/download/geosite.dat"])
    subprocess.run([wget_bin, "-O", f"{assets_dir}geoip.dat", "https://github.com/chocolate4u/Iran-v2ray-rules/releases/latest/download/geoip.dat"])

    # Restart Docker containers using docker-compose
    subprocess.run(["docker", "compose", "-f", "/Marzban-node/docker-compose.yml", "down"])
    subprocess.run(["docker", "compose", "-f", "/Marzban-node/docker-compose.yml", "up", "-d"])

if __name__ == "__main__":
    main()
