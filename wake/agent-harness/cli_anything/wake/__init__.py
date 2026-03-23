import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('wake running')
@cli.command()
def start(): click.echo('wake started')
if __name__ == '__main__': cli()
