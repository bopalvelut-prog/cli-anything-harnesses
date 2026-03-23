import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('primitives running')
@cli.command()
def start(): click.echo('primitives started')
if __name__ == '__main__': cli()
