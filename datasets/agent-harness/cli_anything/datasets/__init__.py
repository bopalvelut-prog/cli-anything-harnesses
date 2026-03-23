import click
@click.group()
def cli(): pass
@cli.command()
def list(): click.echo('Datasets list')
@cli.command()
def load(): click.echo('Datasets load')
if __name__ == '__main__': cli()
