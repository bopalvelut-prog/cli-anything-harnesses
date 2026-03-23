import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('mountain running')
@cli.command()
def start(): click.echo('mountain started')
if __name__ == '__main__': cli()
