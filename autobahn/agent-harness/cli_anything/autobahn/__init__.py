import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('autobahn running')
@cli.command()
def start(): click.echo('autobahn started')
if __name__ == '__main__': cli()
