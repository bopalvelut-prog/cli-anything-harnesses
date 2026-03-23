import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('deskreen running')
@cli.command()
def start(): click.echo('deskreen started')
if __name__ == '__main__': cli()
