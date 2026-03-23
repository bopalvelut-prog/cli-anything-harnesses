import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('glooedge running')
@cli.command()
def start(): click.echo('glooedge started')
if __name__ == '__main__': cli()
