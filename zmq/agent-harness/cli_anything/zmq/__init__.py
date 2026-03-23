import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('zmq running')
@cli.command()
def start(): click.echo('zmq started')
if __name__ == '__main__': cli()
