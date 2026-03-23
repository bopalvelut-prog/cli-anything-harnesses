import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('mapbox running')
@cli.command()
def start(): click.echo('mapbox started')
if __name__ == '__main__': cli()
