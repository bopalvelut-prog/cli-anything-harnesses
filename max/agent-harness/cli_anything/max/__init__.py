import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('max running')
@cli.command()
def start(): click.echo('max started')
if __name__ == '__main__': cli()
