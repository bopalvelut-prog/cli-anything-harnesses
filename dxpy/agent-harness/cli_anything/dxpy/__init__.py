import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('dxpy running')
@cli.command()
def start(): click.echo('dxpy started')
if __name__ == '__main__': cli()
