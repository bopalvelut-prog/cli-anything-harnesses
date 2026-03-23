import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('marshmallow running')
@cli.command()
def start(): click.echo('marshmallow started')
if __name__ == '__main__': cli()
