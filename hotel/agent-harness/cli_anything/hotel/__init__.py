import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('hotel running')
@cli.command()
def start(): click.echo('hotel started')
if __name__ == '__main__': cli()
