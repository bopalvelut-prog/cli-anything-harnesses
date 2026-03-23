import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('silent running')
@cli.command()
def start(): click.echo('silent started')
if __name__ == '__main__': cli()
