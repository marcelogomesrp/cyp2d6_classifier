import sys

import click

from cyp2d6_classifier.core.activity_score import calculate_diplotype_activity_score


@click.group()
def main() -> None:
    pass


cli = main


@main.command()
def about() -> None:
    click.echo("CYP2D6 Metabolizer Classifier - CPIC Guidelines")


@main.command()
@click.argument("diplotype", type=str)
def score(diplotype: str) -> None:
    try:
        activity_score: float = calculate_diplotype_activity_score(diplotype)
        click.echo(f"Activity Score: {activity_score}")
    except ValueError as e:
        click.echo(f"Error: {e}", err=True)
        sys.exit(1)


if __name__ == "__main__":
    main()
