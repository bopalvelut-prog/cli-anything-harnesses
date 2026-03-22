import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def sync(): click.echo('Standard Notes sync')
@cli.command()
def notes(): click.echo('Standard Notes')
if __name__ == '__main__': cli()
