import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('techno running')
@cli.command()
def start(): click.echo('techno started')
if __name__ == '__main__': cli()
