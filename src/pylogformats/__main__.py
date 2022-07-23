"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """PyLogFormats."""


if __name__ == "__main__":
    main(prog_name="pylogformats")  # pragma: no cover
