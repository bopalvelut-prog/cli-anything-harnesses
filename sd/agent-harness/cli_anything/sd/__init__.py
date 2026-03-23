import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('sd running')
@cli.command()
def start(): click.echo('sd started')
if __name__ == '__main__': cli()
