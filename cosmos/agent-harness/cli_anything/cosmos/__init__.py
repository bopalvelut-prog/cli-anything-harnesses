import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def node(): click.echo('Cosmos node')
@cli.command()
def ibc(): click.echo('Cosmos IBC')
if __name__ == '__main__': cli()
