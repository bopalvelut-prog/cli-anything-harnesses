import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('azkaban running')
@cli.command()
def start(): click.echo('azkaban started')
if __name__ == '__main__': cli()
