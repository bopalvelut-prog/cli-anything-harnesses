import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def start(): click.echo('Zoom meeting started')
@cli.command()
def list(): click.echo('Zoom meetings')
if __name__ == '__main__': cli()
