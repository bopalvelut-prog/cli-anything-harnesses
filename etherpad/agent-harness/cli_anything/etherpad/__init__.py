import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('Etherpad running')
@cli.command()
def pads(): click.echo('Etherpad pads')
if __name__ == '__main__': cli()
