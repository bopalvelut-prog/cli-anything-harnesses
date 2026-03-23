import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('nothing running')
@cli.command()
def start(): click.echo('nothing started')
if __name__ == '__main__': cli()
