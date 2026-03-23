import click
@click.group()
def cli(): pass
@cli.command()
def list(): click.echo('Images')
@cli.command()
def create(): click.echo('Create image')
if __name__ == '__main__': cli()
