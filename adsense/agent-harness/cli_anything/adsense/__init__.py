import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('adsense running')
@cli.command()
def start(): click.echo('adsense started')
if __name__ == '__main__': cli()
