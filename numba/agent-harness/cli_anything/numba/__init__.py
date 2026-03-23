import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('numba running')
@cli.command()
def start(): click.echo('numba started')
if __name__ == '__main__': cli()
