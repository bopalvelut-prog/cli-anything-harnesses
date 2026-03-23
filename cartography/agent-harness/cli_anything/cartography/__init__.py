import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('cartography running')
@cli.command()
def start(): click.echo('cartography started')
if __name__ == '__main__': cli()
