import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('quic running')
@cli.command()
def start(): click.echo('quic started')
if __name__ == '__main__': cli()
