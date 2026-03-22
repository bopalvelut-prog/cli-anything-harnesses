import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def open(): click.echo('KeePassXC opened')
@cli.command()
def list(): click.echo('KeePassXC entries')
if __name__ == '__main__': cli()
