import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def list(): click.echo('Photos list')
@cli.command()
def sync(): click.echo('Photos sync')
if __name__ == '__main__': cli()
