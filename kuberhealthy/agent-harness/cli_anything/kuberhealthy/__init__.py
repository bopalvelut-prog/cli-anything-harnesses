import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('kuberhealthy running')
@cli.command()
def start(): click.echo('kuberhealthy started')
if __name__ == '__main__': cli()
