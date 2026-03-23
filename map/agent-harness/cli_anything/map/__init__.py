import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('map running')
@cli.command()
def start(): click.echo('map started')
if __name__ == '__main__': cli()
