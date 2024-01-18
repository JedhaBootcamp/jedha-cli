import platform
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
    return pkg_resources.resource_filename("src", f"labs/{labname}.yaml")


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
            command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True
        )
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def docker_is_installed() -> bool:
    """
    Check if Docker is installed on the machine.

    Returns:
        bool: True if Docker is installed, False otherwise.
    """
    return run_command(["docker", "--version"])


def docker_compose_v2_is_installed() -> bool:
    """
    Check if Docker Compose V2 is installed on the machine.

    Returns:
        bool: True if Docker Compose is installed, False otherwise.
    """
    return run_command(["docker", "compose", "version"])


def docker_compose_v1_is_installed() -> bool:
    """
    Check if Docker Compose V1 is installed on the machine.

    Returns:
        bool: True if Docker Compose is installed, False otherwise.
    """
    return run_command(["docker-compose", "--version"])


def docker_requires_sudo() -> bool:
    """
    Check if Docker requires sudo.

    Returns:
        bool: True if Docker requires sudo, False otherwise.
    """
    return run_command(["docker", "ps"])


def get_docker_compose_command(args: List[str]) -> List[str]:
    """
    Manage the Docker command depending on the OS.

    Args:
        args (List[str]): The arguments to pass to the Docker compose command.
    """
    if not docker_is_installed():
        print("Docker not found. Please install it.")
        raise typer.Exit(code=1)
    if docker_compose_v2_is_installed():
        args.insert(0, "docker")
        args.insert(1, "compose")
    elif docker_compose_v1_is_installed():
        args.insert(0, "docker-compose")
    else:
        print(
            "Docker Compose (either V1 or V2) not found. Please install Docker Desktop or docker-compose."
        )
        raise typer.Exit(code=1)
    if platform.system() != "Darwin" or docker_requires_sudo():
        args.insert(0, "sudo")
    return args
