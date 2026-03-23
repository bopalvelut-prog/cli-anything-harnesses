import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('pint running')
@cli.command()
def start(): click.echo('pint started')
if __name__ == '__main__': cli()
