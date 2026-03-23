import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('till running')
@cli.command()
def start(): click.echo('till started')
if __name__ == '__main__': cli()
