import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('psychopy running')
@cli.command()
def start(): click.echo('psychopy started')
if __name__ == '__main__': cli()
