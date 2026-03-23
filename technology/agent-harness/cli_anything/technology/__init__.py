import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('technology running')
@cli.command()
def start(): click.echo('technology started')
if __name__ == '__main__': cli()
