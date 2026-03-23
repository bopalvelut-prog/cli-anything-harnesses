import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('grid running')
@cli.command()
def start(): click.echo('grid started')
if __name__ == '__main__': cli()
