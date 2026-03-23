import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('store running')
@cli.command()
def start(): click.echo('store started')
if __name__ == '__main__': cli()
