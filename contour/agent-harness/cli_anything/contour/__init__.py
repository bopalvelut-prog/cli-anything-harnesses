import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('contour running')
@cli.command()
def start(): click.echo('contour started')
if __name__ == '__main__': cli()
