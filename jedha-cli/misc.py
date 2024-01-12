import subprocess
from typing import List

import pkg_resources
import typer


def get_lab_config_file(labname: str) -> str:
    """
    Get the content of the lab's Docker Compose configuration file.
    Args:
        labname (str): The name of the lab.
    Returns:
        str: The content of the lab's Docker Compose configuration file.
    """
    return pkg_resources.resource_filename("jedhacli", f"labs/{labname}.yaml")


def run_command(command: List[str]) -> bool:
    """
    Utility function to run a command and return True if it succeeds.

    Args:
        command (List[str]): The command to run as a list of strings.
    Returns:
        bool: True if the command succeeds, False otherwise.
    """
    try:
        subprocess.run(
            command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True
        )
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def test_environment_decorator():
    """
    Check if Docker and Docker-Compose are installed on the machine.
    """
    docker_installed = run_command(["docker", "--version"])
    docker_compose_installed = run_command(["docker", "compose", "version"])
    old_version_installed = run_command(["docker-compose", "--version"])

    if not docker_installed:
        print("Docker not found. Please install it.")
        raise typer.Exit(code=1)

    if not docker_compose_installed:
        if old_version_installed:
            print(
                "You have an old version of docker-compose, please go on the official website to switch to V2"
            )
        else:
            print("Docker Compose not found. Please install Docker Desktop")
        raise typer.Exit(code=1)
