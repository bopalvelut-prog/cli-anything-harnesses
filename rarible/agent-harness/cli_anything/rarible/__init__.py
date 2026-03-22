import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def list(): click.echo('Rarible listings')
@cli.command()
def buy(): click.echo('Rarible buy')
if __name__ == '__main__': cli()
