import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('much running')
@cli.command()
def start(): click.echo('much started')
if __name__ == '__main__': cli()
