import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('beneath running')
@cli.command()
def start(): click.echo('beneath started')
if __name__ == '__main__': cli()
