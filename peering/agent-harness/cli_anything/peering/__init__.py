import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('peering running')
@cli.command()
def start(): click.echo('peering started')
if __name__ == '__main__': cli()
