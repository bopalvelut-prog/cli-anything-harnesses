import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('xorg running')
@cli.command()
def start(): click.echo('xorg started')
if __name__ == '__main__': cli()
