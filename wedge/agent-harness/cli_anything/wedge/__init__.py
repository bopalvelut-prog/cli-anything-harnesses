import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('wedge running')
@cli.command()
def start(): click.echo('wedge started')
if __name__ == '__main__': cli()
