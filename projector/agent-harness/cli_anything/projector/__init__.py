import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('projector running')
@cli.command()
def start(): click.echo('projector started')
if __name__ == '__main__': cli()
