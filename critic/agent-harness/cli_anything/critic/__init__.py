import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('critic running')
@cli.command()
def start(): click.echo('critic started')
if __name__ == '__main__': cli()
