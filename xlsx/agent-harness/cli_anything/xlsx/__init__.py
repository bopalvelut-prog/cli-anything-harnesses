import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('xlsx running')
@cli.command()
def start(): click.echo('xlsx started')
if __name__ == '__main__': cli()
