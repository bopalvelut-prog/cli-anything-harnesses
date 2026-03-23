import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('rough running')
@cli.command()
def start(): click.echo('rough started')
if __name__ == '__main__': cli()
