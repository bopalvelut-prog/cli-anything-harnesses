import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('roaring running')
@cli.command()
def start(): click.echo('roaring started')
if __name__ == '__main__': cli()
