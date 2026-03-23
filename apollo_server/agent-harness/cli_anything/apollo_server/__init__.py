import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('apollo_server running')
@cli.command()
def start(): click.echo('apollo_server started')
if __name__ == '__main__': cli()
