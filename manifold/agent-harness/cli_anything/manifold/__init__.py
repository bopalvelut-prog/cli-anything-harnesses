import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('manifold running')
@cli.command()
def start(): click.echo('manifold started')
if __name__ == '__main__': cli()
