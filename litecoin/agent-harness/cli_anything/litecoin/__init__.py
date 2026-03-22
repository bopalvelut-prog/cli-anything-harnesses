import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def node(): click.echo('Litecoin node')
@cli.command()
def wallet(): click.echo('Litecoin wallet')
if __name__ == '__main__': cli()
