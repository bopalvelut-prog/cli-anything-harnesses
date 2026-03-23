import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('pytest_xdist running')
@cli.command()
def start(): click.echo('pytest_xdist started')
if __name__ == '__main__': cli()
