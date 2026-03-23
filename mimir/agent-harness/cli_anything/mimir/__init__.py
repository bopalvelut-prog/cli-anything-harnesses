import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('mimir running')
@cli.command()
def start(): click.echo('mimir started')
if __name__ == '__main__': cli()
