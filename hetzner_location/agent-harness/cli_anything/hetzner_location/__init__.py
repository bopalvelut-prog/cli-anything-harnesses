import click
@click.group()
def cli(): pass
@cli.command()
def list(): click.echo('Locations')
if __name__ == '__main__': cli()
