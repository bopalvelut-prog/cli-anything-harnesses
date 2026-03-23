import click
@click.group()
def cli(): pass
@cli.command()
def query(): click.echo('Azure SQL query')
@cli.command()
def servers(): click.echo('Azure SQL servers')
if __name__ == '__main__': cli()
