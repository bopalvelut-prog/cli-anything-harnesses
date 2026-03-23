import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('embed running')
@cli.command()
def start(): click.echo('embed started')
if __name__ == '__main__': cli()
