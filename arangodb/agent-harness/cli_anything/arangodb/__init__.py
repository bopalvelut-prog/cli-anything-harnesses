import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('arangodb running')
@cli.command()
def start(): click.echo('arangodb started')
if __name__ == '__main__': cli()
