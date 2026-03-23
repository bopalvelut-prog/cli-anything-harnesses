import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('magma running')
@cli.command()
def start(): click.echo('magma started')
if __name__ == '__main__': cli()
