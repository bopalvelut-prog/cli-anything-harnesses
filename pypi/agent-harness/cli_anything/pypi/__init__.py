import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('pypi running')
@cli.command()
def start(): click.echo('pypi started')
if __name__ == '__main__': cli()
