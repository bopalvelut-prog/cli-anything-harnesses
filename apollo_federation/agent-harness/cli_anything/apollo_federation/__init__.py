import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('apollo_federation running')
@cli.command()
def start(): click.echo('apollo_federation started')
if __name__ == '__main__': cli()
