import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('pebble running')
@cli.command()
def start(): click.echo('pebble started')
if __name__ == '__main__': cli()
