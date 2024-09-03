"""
Lab Testing Script

Purpose:
---------
This script automates the testing of cyber security labs defined in `labs.yaml`. 
It starts each lab, checks its availability via ping, stops the lab, and generates 
a summary report.

Usage:
-------
1. Ensure Docker and Poetry are installed and running.
2. Install dependencies: `poetry install`.
3. Run the script: `poetry run python tests/your_test_script.py`.
4. Review the console report to see which labs passed or failed.

Prerequisites:
---------------
- Docker
- Poetry
- Ping utility
"""

import yaml
import subprocess
import time
import sys
import shutil
from tabulate import tabulate


def check_command_availability(command):
    """Check if a command is available on the system."""
    return shutil.which(command) is not None


def check_docker_running():
    """Check if Docker is running."""
    try:
        subprocess.check_output(["docker", "info"], stderr=subprocess.STDOUT)
        return True
    except subprocess.CalledProcessError:
        return False


def start_lab(name):
    """Start the lab using `poetry run python -m src.main start {name}`."""
    try:
        print(f"Starting lab {name}...")
        subprocess.check_output(
            ["poetry", "run", "python", "-m", "src.main", "start", name],
            stderr=subprocess.STDOUT,
        )
    except subprocess.CalledProcessError as e:
        print(f"Failed to start lab {name}. Error: {e.output.decode()}")
        sys.exit(1)


def stop_lab(name):
    """Stop the lab using `poetry run python -m src.main stop {name}`."""
    try:
        print(f"Stopping lab {name}...")
        subprocess.check_output(
            ["poetry", "run", "python", "-m", "src.main", "stop", name, "--force"],
            stderr=subprocess.STDOUT,
        )
    except subprocess.CalledProcessError as e:
        print(f"Failed to stop lab {name}. Error: {e.output.decode()}")
        sys.exit(1)


def ping_ip(ip):
    """Ping an IP address and return True if the IP is reachable, otherwise False."""
    try:
        subprocess.check_output(["ping", "-c", "1", ip], stderr=subprocess.STDOUT)
        return True
    except subprocess.CalledProcessError:
        return False


def wait_for_lab(ip, timeout=60):
    """Wait for the lab to be up by pinging the IP until it's reachable or timeout."""
    print(f"Waiting for the lab to be up at {ip}...")
    start_time = time.time()
    while time.time() - start_time < timeout:
        if ping_ip(ip):
            return True
        time.sleep(5)
    return False


prerequisites = {"docker": "docker", "ping": "ping"}

missing_tools = [
    tool
    for tool, command in prerequisites.items()
    if not check_command_availability(command)
]
docker_running = check_docker_running()

if missing_tools:
    print(
        f"Missing tools: {', '.join(missing_tools)}. Please install them and ensure they are in your PATH."
    )
    sys.exit(1)

if not docker_running:
    print("Docker is installed but not running. Please start Docker and try again.")
    sys.exit(1)

print("All prerequisites are met. Proceeding with the lab checks...\n")

with open("src/labs.yaml", "r") as file:
    labs = yaml.safe_load(file)

report_data = []

for lab in labs:
    print(f"Checking lab: {lab.get('name')}...")
    ip = lab.get("ip")
    name = lab.get("name")

    if not ip or "and" in ip or "/" in ip:
        print(f"Skipping {name}: Invalid or multiple IPs.")
        continue

    start_lab(name)

    if wait_for_lab(ip):
        print(f"{name} ({ip}) is up and running.")
        status = "succeed"
    else:
        print(f"Failed to start {name} or it's not reachable at {ip}.")
        status = "fail"

    report_data.append([name, ip, status])

    stop_lab(name)
    print("\n")

print("Final Report:\n")
headers = ["Lab Name", "IP Address", "Status"]
print(tabulate(report_data, headers=headers, tablefmt="grid"))
