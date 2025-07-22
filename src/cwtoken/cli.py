import click
from .utils import test_connection
from .gui import main as run_gui

@click.group()
def cli():
    """cwtoken command-line interface."""
    pass

cli.add_command(test_connection, name="test-connection")

@cli.command()
def gui():
    """Launch the GUI app"""
    run_gui()

if __name__ == "__main__":
    cli()
