"""Console script for adbloater."""

import os
import sys
import click

import logging


DISABLE_CMD = False  # disable shell command executions (for testing)
# import datetime as dt

# configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.FileHandler("debloater.log"), logging.StreamHandler()],
)

log = logging.getLogger()


class bcolors:
    """terminal color definitions"""

    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def shell_cmd(cmd):
    """run shell command, echo to screen"""

    print(bcolors.OKCYAN + ">" + cmd + bcolors.ENDC)
    log.info(">" + cmd)
    if not DISABLE_CMD:
        os.system(cmd)


def uninstall_pkg(name: str):
    """uninstall a package"""
    shell_cmd("adb shell pm uninstall --user 0 " + name)


def restore_pkg(name: str):
    """restore previously removed package"""
    shell_cmd("adb shell cmd package install-existing " + name)


def get_packages_to_remove(filename: str, symbol="#") -> list:
    """read commented out lines to get packages"""
    with open(filename, "r", encoding="utf-8") as fid:
        lines = fid.readlines()

    packages = []

    for line in lines:
        if line[0] == symbol:
            packages.append(line.split(":")[1].strip())

    return packages


@click.command()
@click.option("--save", help="save packages to packages.txt", is_flag=True)
def get_packages(save):
    """get list of packages from device"""

    if not save:
        shell_cmd("adb shell pm list packages")
    else:
        shell_cmd("adb shell pm list packages > packages.txt")


@click.command()
def uninstall():
    """uninstall marked packages in packages.txt"""

    packages = get_packages_to_remove("packages.txt")
    print("Uninstalling packages:")
    for pkg in packages:
        print(pkg)

    if click.confirm("Are you sure?"):
        for pkg in packages:
            uninstall_pkg(pkg)


@click.command()
def restore():
    """put back packages marked packages in packages.txt"""

    packages = get_packages_to_remove("packages.txt")
    print("Installing packages:")
    for pkg in packages:
        print(pkg)

    if click.confirm("Are you sure?"):
        for pkg in packages:
            restore_pkg(pkg)


@click.group()
def cli():
    pass


cli.add_command(get_packages)
cli.add_command(uninstall)
cli.add_command(restore)


if __name__ == "__main__":
    cli()
