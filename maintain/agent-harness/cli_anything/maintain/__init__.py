import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('maintain running')
@cli.command()
def start(): click.echo('maintain started')
if __name__ == '__main__': cli()
