import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def list(): click.echo('Google Drive files')
@cli.command()
def sync(): click.echo('Google Drive sync')
if __name__ == '__main__': cli()
