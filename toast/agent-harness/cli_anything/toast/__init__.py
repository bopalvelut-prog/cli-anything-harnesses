import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('toast running')
@cli.command()
def start(): click.echo('toast started')
if __name__ == '__main__': cli()
