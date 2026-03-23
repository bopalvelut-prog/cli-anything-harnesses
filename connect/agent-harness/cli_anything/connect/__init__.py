import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('connect running')
@cli.command()
def start(): click.echo('connect started')
if __name__ == '__main__': cli()
