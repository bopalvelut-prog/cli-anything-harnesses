import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('aperture running')
@cli.command()
def start(): click.echo('aperture started')
if __name__ == '__main__': cli()
