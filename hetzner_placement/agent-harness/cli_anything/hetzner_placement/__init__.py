import click
@click.group()
def cli(): pass
@cli.command()
def list(): click.echo('Placements')
@cli.command()
def create(): click.echo('Create placement')
if __name__ == '__main__': cli()
