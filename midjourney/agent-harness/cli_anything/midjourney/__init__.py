import click
@click.group()
def cli(): pass
@cli.command()
def imagine(): click.echo('Midjourney imagine')
@cli.command()
def list(): click.echo('Midjourney images')
if __name__ == '__main__': cli()
