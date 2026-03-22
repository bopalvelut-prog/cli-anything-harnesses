import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def node(): click.echo('Cardano node')
@cli.command()
def wallet(): click.echo('Cardano wallet')
if __name__ == '__main__': cli()
