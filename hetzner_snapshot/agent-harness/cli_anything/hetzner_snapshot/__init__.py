import click
@click.group()
def cli(): pass
@cli.command()
def list(): click.echo('Snapshots')
@cli.command()
def create(): click.echo('Create snapshot')
if __name__ == '__main__': cli()
