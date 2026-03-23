import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('networkmanager running')
@cli.command()
def start(): click.echo('networkmanager started')
if __name__ == '__main__': cli()
