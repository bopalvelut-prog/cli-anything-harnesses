import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def node(): click.echo('Base node')
@cli.command()
def bridge(): click.echo('Base bridge')
if __name__ == '__main__': cli()
