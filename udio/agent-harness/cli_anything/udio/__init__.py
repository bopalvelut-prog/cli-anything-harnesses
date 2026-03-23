import click
@click.group()
def cli(): pass
@cli.command()
def generate(): click.echo('Udio generate')
@cli.command()
def list(): click.echo('Udio list')
if __name__ == '__main__': cli()
