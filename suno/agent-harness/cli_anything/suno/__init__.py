import click
@click.group()
def cli(): pass
@cli.command()
def generate(): click.echo('Suno generate')
@cli.command()
def list(): click.echo('Suno list')
if __name__ == '__main__': cli()
