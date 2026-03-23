import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('stock running')
@cli.command()
def start(): click.echo('stock started')
if __name__ == '__main__': cli()
