import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def node(): click.echo('Pirate node')
@cli.command()
def wallet(): click.echo('Pirate wallet')
if __name__ == '__main__': cli()
