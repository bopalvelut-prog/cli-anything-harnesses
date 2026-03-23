import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('meteor running')
@cli.command()
def start(): click.echo('meteor started')
if __name__ == '__main__': cli()
