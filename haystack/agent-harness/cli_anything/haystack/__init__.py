import click
@click.group()
def cli(): pass
@cli.command()
def query(): click.echo('Haystack query')
@cli.command()
def pipeline(): click.echo('Haystack pipeline')
if __name__ == '__main__': cli()
