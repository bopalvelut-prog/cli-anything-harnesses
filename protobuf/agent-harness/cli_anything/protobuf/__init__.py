import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('protobuf running')
@cli.command()
def start(): click.echo('protobuf started')
if __name__ == '__main__': cli()
