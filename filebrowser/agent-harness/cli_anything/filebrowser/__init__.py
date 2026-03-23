import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('filebrowser running')
@cli.command()
def start(): click.echo('filebrowser started')
if __name__ == '__main__': cli()
