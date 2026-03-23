import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('honor running')
@cli.command()
def start(): click.echo('honor started')
if __name__ == '__main__': cli()
