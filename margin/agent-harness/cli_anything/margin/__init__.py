import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('margin running')
@cli.command()
def start(): click.echo('margin started')
if __name__ == '__main__': cli()
