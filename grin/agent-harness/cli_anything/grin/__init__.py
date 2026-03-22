import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def node(): click.echo('Grin node')
@cli.command()
def wallet(): click.echo('Grin wallet')
if __name__ == '__main__': cli()
