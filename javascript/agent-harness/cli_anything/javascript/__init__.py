import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('javascript running')
@cli.command()
def start(): click.echo('javascript started')
if __name__ == '__main__': cli()
