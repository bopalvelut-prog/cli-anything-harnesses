import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('pink running')
@cli.command()
def start(): click.echo('pink started')
if __name__ == '__main__': cli()
