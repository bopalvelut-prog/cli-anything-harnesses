import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('sea running')
@cli.command()
def start(): click.echo('sea started')
if __name__ == '__main__': cli()
