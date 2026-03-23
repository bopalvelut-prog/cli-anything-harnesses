import click
@click.group()
def cli(): pass
@cli.command()
def databases(): click.echo('Cosmos databases')
@cli.command()
def query(): click.echo('Cosmos query')
if __name__ == '__main__': cli()
