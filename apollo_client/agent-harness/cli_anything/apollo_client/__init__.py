import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('apollo_client running')
@cli.command()
def start(): click.echo('apollo_client started')
if __name__ == '__main__': cli()
