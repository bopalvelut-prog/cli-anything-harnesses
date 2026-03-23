import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('materialui running')
@cli.command()
def start(): click.echo('materialui started')
if __name__ == '__main__': cli()
