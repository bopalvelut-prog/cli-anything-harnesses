import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('linkedin running')
@cli.command()
def start(): click.echo('linkedin started')
if __name__ == '__main__': cli()
