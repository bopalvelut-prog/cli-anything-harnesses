import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def order(): click.echo('Serum order')
@cli.command()
def book(): click.echo('Serum orderbook')
if __name__ == '__main__': cli()
