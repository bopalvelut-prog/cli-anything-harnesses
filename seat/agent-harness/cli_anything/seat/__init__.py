import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('seat running')
@cli.command()
def start(): click.echo('seat started')
if __name__ == '__main__': cli()
