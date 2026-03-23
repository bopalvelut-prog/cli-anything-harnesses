import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('reactive running')
@cli.command()
def start(): click.echo('reactive started')
if __name__ == '__main__': cli()
