import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def node(): click.echo('Polygon node')
@cli.command()
def bridge(): click.echo('Polygon bridge')
if __name__ == '__main__': cli()
