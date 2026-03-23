import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('borrow running')
@cli.command()
def start(): click.echo('borrow started')
if __name__ == '__main__': cli()
