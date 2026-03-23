import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('backpack running')
@cli.command()
def start(): click.echo('backpack started')
if __name__ == '__main__': cli()
