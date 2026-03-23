import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('dagger running')
@cli.command()
def start(): click.echo('dagger started')
if __name__ == '__main__': cli()
