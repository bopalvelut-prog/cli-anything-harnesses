import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def node(): click.echo('Kaspa node')
@cli.command()
def wallet(): click.echo('Kaspa wallet')
if __name__ == '__main__': cli()
