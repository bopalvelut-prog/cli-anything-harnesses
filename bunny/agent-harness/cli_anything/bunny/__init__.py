import click
@click.group()
def cli(): pass
@cli.command()
def purge(): click.echo('Bunny CDN purge')
@cli.command()
def list(): click.echo('Bunny CDN list')
if __name__ == '__main__': cli()
