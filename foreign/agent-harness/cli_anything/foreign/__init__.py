import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('foreign running')
@cli.command()
def start(): click.echo('foreign started')
if __name__ == '__main__': cli()
