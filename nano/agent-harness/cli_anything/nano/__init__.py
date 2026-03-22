import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def node(): click.echo('Nano node')
@cli.command()
def wallet(): click.echo('Nano wallet')
if __name__ == '__main__': cli()
