import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('family running')
@cli.command()
def start(): click.echo('family started')
if __name__ == '__main__': cli()
