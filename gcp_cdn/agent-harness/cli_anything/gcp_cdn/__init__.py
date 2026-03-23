import click
@click.group()
def cli(): pass
@cli.command()
def purge(): click.echo('Google CDN purge')
@cli.command()
def backends(): click.echo('Google CDN backends')
if __name__ == '__main__': cli()
