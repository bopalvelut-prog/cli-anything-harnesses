import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('qgis running')
@cli.command()
def start(): click.echo('qgis started')
if __name__ == '__main__': cli()
