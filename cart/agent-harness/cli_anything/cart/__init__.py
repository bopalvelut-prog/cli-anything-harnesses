import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('cart running')
@cli.command()
def start(): click.echo('cart started')
if __name__ == '__main__': cli()
