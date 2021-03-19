import click
from flask.cli import with_appcontext


@click.group()
def cli():
    """Main entry point"""

if __name__ == "__main__":
    cli()
