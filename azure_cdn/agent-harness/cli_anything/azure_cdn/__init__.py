import click
@click.group()
def cli(): pass
@cli.command()
def purge(): click.echo('Azure CDN purge')
@cli.command()
def endpoints(): click.echo('Azure CDN endpoints')
if __name__ == '__main__': cli()
