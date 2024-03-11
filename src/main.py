#! /usr/bin/python3

import os
import subprocess
from typing import Annotated, List

import pkg_resources
import typer
from rich import print
from rich.console import Console
from rich.table import Table
from yaml import load

try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader

from .misc import get_docker_compose_command, get_lab_config_file, check_for_updates

app = typer.Typer(
    name="jedhacli",
    help="""
A CLI to manage the labs for Cybersecurity Bootcamp at Jedha (https://jedha.co).

⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n
⠀⠀⠀⠀⣠⣧⠷⠆⠀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀\n
⠀⠀⣐⣢⣤⢖⠒⠪⣭⣶⣿⣦⠀⠀⠀⠀⠀⠀⠀\n
⠀⢸⣿⣿⣿⣌⠀⢀⣿⠁⢹⣿⡇⠀⠀⠀⠀⠀⠀\n
⠀⢸⣿⣿⣿⣿⣿⡿⠿⢖⡪⠅⢂⠀⠀⠀⠀⠀⠀\n
⠀⠀⢀⣔⣒⣒⣂⣈⣉⣄⠀⠺⣿⠿⣦⡀⠀⠀⠀\n
⠀⡴⠛⣉⣀⡈⠙⠻⣿⣿⣷⣦⣄⠀⠛⠻⠦⠀⠀\n
⡸⠁⢾⣿⣿⣁⣤⡀⠹⣿⣿⣿⣿⣿⣷⣶⣶⣤⠀\n
⡇⣷⣿⣿⣿⣿⣿⡇⠀⣿⣿⣿⣿⣿⣿⡿⠿⣿⡀\n
⡇⢿⣿⣿⣿⣟⠛⠃⠀⣿⣿⣿⡿⠋⠁⣀⣀⡀⠃\n
⢻⡌⠀⠿⠿⠿⠃⠀⣼⣿⣿⠟⠀⣠⣄⣿⣿⡣⠀\n
⠈⢿⣶⣤⣤⣤⣴⣾⣿⣿⡏⠀⣼⣿⣿⣿⡿⠁⠀\n
⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⠀⠀⣩⣿⡿⠋⠀⠀⠀\n
⠀⠀⠀⠀⠈⠙⠛⠿⠿⠿⠇⠀⠉⠁⠀⠀⠀⠀⠀\n
    """,
    epilog="Made with ❤️ by the Jedha Bootcamp Team",
    no_args_is_help=True,
)

console = Console()


# @app.command("config", help="Configure the CLI.")
# def config():
#     """
#     Configure the CLI by prompting the user for the required information.
#     """
#     pass


@app.command("list", help="List all the labs available.")
def list() -> List[str]:
    """
    List all the labs available.
    """
    labs_yaml_file = pkg_resources.resource_filename("src", "labs.yaml")
    with open(labs_yaml_file, "r") as f:
        filename_array = load(f, Loader=Loader)

    table = Table("Name", "IP", "Description", show_lines=True, title="Available Labs")
    for i in filename_array:
        table.add_row(i["name"], i["ip"], i["description"])
    console.print(table)


@app.command("status", help="Show the running labs.")
def status(labname: str):
    """
    Show the running labs.
    """
    lab_config_file = get_lab_config_file(labname)
    if not lab_config_file or not os.path.exists(lab_config_file):
        print("Docker Compose file not found for the specified lab.")
        return

    try:
        command = get_docker_compose_command(["--file", lab_config_file, "ps"])
        subprocess.run(
            command,
            check=True,
        )
    except subprocess.CalledProcessError as e:
        print(
            f"Failed to show status of lab {labname}: Error with the docker compose file or Docker itself"
        )


@app.command("start", help="Start a specific lab environment.")
def start(labname: str):
    """
    Start a lab.

    Args:
        labname (str): Name of the lab.
    """
    lab_config_file = get_lab_config_file(labname)
    if not lab_config_file or not os.path.exists(lab_config_file):
        print("Docker Compose file not found for the specified lab.")
        return

    try:
        command = get_docker_compose_command(["--file", lab_config_file, "up", "-d"])
        subprocess.run(
            command,
            check=True,
        )
        print(f"Lab {labname} started successfully.")
    except subprocess.CalledProcessError as e:
        print(
            f"Failed to start lab {labname}: Error with the docker compose file or Docker itself"
        )


@app.command("restart", help="Restart a lab.")
def restart(labname: str):
    """
    Restart a lab.

    Args:
        labname (str): Name of the lab.
    """
    lab_config_file = get_lab_config_file(labname)
    if not lab_config_file or not os.path.exists(lab_config_file):
        print("Docker Compose file not found for the specified lab.")
        return

    try:
        command = get_docker_compose_command(["--file", lab_config_file, "restart"])
        subprocess.run(
            command,
            check=True,
        )
        print(f"Lab {labname} restarted successfully.")
    except subprocess.CalledProcessError as e:
        print(
            f"Failed to restart lab {labname}: Error with the docker compose file or Docker itself"
        )


@app.command("stop", help="Stop and clean up a specific lab environment.")
def stop(
    labname: str,
    force: Annotated[
        bool, typer.Option(prompt="Are you sure you want to stop the lab?")
    ],
):
    """
    Stop and clean up a specific lab environment.

    Args:
        labname (str): Name of the lab.
    """
    lab_config_file = get_lab_config_file(labname)
    if not lab_config_file or not os.path.exists(lab_config_file):
        print("Docker Compose file not found for the specified lab.")
        return

    if force:
        try:
            command = get_docker_compose_command(
                [
                    "--file",
                    lab_config_file,
                    "down",
                    "--remove-orphans",
                    "--volumes",
                ],
            )
            subprocess.run(
                command,
                check=True,
            )
            print(f"Lab {labname} taken down successfully.")
        except subprocess.CalledProcessError as e:
            print(
                f"Failed to take down lab {labname}: Error with the docker compose file or Docker itself"
            )
    else:
        print("Aborting.")


@app.command(
    "remove",
    help="Remove definitively a specific lab environment. Do it to free your disk space.",
)
def remove(
    labname: str,
    force: Annotated[
        bool, typer.Option(prompt="Are you sure you want to remove the lab?")
    ],
):
    """
    Remove a lab.

    Args:
        labname (str): Name of the lab.
    """
    lab_config_file = get_lab_config_file(labname)
    if not lab_config_file or not os.path.exists(lab_config_file):
        print("Docker Compose file not found for the specified lab.")
        return

    if force:
        try:
            command = get_docker_compose_command(
                [
                    "--file",
                    lab_config_file,
                    "down",
                    "--remove-orphans",
                    "--volumes",
                    "--rmi",
                    "all",
                ]
            )
            subprocess.run(
                command,
                check=True,
            )
            print(f"Lab {labname} definitively removed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to clean lab {labname}.")
    else:
        print("Aborting.")


def main():
    check_for_updates()
    app()


if __name__ == "__main__":
    main()
