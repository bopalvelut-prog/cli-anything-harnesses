import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('spread running')
@cli.command()
def start(): click.echo('spread started')
if __name__ == '__main__': cli()
