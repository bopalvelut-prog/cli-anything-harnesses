import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('product running')
@cli.command()
def start(): click.echo('product started')
if __name__ == '__main__': cli()
