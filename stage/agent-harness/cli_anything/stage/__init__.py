import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('stage running')
@cli.command()
def start(): click.echo('stage started')
if __name__ == '__main__': cli()
