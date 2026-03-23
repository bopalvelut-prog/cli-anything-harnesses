import click
@click.group()
def cli(): pass
@cli.command()
def collections(): click.echo('Firestore collections')
@cli.command()
def query(): click.echo('Firestore query')
if __name__ == '__main__': cli()
