import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('shall running')
@cli.command()
def start(): click.echo('shall started')
if __name__ == '__main__': cli()
