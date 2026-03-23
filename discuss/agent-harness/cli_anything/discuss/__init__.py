import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('discuss running')
@cli.command()
def start(): click.echo('discuss started')
if __name__ == '__main__': cli()
