import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('tidyverse running')
@cli.command()
def start(): click.echo('tidyverse started')
if __name__ == '__main__': cli()
