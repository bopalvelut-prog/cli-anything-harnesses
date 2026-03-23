import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('floor running')
@cli.command()
def start(): click.echo('floor started')
if __name__ == '__main__': cli()
