import click


@click.group()
def main() -> None:
    pass


@main.command()
def about() -> None:
    click.echo("CYP2D6 Metabolizer Classifier - CPIC Guidelines")


if __name__ == "__main__":
    main()
