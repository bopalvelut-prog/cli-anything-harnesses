import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('rudder running')
@cli.command()
def start(): click.echo('rudder started')
if __name__ == '__main__': cli()
