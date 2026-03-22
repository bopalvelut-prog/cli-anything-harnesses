import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def list(): click.echo('OpenSea listings')
@cli.command()
def buy(): click.echo('OpenSea buy')
if __name__ == '__main__': cli()
