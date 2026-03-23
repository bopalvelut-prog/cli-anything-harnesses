import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('latter running')
@cli.command()
def start(): click.echo('latter started')
if __name__ == '__main__': cli()
