import click
@click.group()
def cli(): pass
@cli.command()
def query(): click.echo('D1 query')
@cli.command()
def list(): click.echo('D1 list')
if __name__ == '__main__': cli()
