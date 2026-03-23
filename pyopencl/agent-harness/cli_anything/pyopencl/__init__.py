import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('pyopencl running')
@cli.command()
def start(): click.echo('pyopencl started')
if __name__ == '__main__': cli()
