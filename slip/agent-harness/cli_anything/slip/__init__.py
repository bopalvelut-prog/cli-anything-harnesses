import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('slip running')
@cli.command()
def start(): click.echo('slip started')
if __name__ == '__main__': cli()
