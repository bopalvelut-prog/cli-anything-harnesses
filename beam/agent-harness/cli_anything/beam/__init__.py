import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def node(): click.echo('Beam node')
@cli.command()
def wallet(): click.echo('Beam wallet')
if __name__ == '__main__': cli()
