import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('armstrong running')
@cli.command()
def start(): click.echo('armstrong started')
if __name__ == '__main__': cli()
