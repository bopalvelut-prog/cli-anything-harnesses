import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('peerdb running')
@cli.command()
def start(): click.echo('peerdb started')
if __name__ == '__main__': cli()
