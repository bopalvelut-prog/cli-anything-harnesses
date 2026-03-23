import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('vehicle running')
@cli.command()
def start(): click.echo('vehicle started')
if __name__ == '__main__': cli()
