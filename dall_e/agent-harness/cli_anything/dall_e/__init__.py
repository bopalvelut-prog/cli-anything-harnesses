import click
@click.group()
def cli(): pass
@cli.command()
def generate(): click.echo('DALL-E generate')
@cli.command()
def list(): click.echo('DALL-E images')
if __name__ == '__main__': cli()
