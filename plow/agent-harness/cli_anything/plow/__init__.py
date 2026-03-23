import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('plow running')
@cli.command()
def start(): click.echo('plow started')
if __name__ == '__main__': cli()
