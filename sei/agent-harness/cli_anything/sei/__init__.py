import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def node(): click.echo('Sei node')
@cli.command()
def trade(): click.echo('Sei trade')
if __name__ == '__main__': cli()
