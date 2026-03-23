import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('shipyard running')
@cli.command()
def start(): click.echo('shipyard started')
if __name__ == '__main__': cli()
