import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def node(): click.echo('Decred node')
@cli.command()
def wallet(): click.echo('Decred wallet')
if __name__ == '__main__': cli()
