import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('py running')
@cli.command()
def start(): click.echo('py started')
if __name__ == '__main__': cli()
