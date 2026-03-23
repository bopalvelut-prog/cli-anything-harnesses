import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('pyxel running')
@cli.command()
def start(): click.echo('pyxel started')
if __name__ == '__main__': cli()
