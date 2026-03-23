import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('newsblur running')
@cli.command()
def start(): click.echo('newsblur started')
if __name__ == '__main__': cli()
