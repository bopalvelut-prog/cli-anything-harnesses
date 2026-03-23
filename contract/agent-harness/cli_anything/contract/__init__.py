import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('contract running')
@cli.command()
def start(): click.echo('contract started')
if __name__ == '__main__': cli()
