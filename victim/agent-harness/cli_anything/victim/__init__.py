import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('victim running')
@cli.command()
def start(): click.echo('victim started')
if __name__ == '__main__': cli()
