import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('osrm running')
@cli.command()
def start(): click.echo('osrm started')
if __name__ == '__main__': cli()
