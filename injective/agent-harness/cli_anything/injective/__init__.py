import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def node(): click.echo('Injective node')
@cli.command()
def trade(): click.echo('Injective trade')
if __name__ == '__main__': cli()
