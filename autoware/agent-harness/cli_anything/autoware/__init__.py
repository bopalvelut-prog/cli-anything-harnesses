import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('autoware running')
@cli.command()
def start(): click.echo('autoware started')
if __name__ == '__main__': cli()
