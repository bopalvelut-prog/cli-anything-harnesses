import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('pybind11 running')
@cli.command()
def start(): click.echo('pybind11 started')
if __name__ == '__main__': cli()
