import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def node(): click.echo('Zcash node')
@cli.command()
def wallet(): click.echo('Zcash wallet')
if __name__ == '__main__': cli()
