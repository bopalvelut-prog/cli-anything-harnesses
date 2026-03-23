import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('medical running')
@cli.command()
def start(): click.echo('medical started')
if __name__ == '__main__': cli()
