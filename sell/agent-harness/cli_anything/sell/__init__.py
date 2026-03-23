import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('sell running')
@cli.command()
def start(): click.echo('sell started')
if __name__ == '__main__': cli()
