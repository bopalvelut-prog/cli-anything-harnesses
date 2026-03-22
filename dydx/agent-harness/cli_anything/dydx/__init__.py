import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def trade(): click.echo('dYdX trade')
@cli.command()
def position(): click.echo('dYdX position')
if __name__ == '__main__': cli()
