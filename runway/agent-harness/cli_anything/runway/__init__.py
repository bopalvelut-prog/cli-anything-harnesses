import click
@click.group()
def cli(): pass
@cli.command()
def generate(): click.echo('Runway generate')
@cli.command()
def list(): click.echo('Runway list')
if __name__ == '__main__': cli()
