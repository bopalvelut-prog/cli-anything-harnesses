import click
@click.group()
def cli(): pass
@cli.command()
def list(): click.echo('Networks')
@cli.command()
def create(): click.echo('Create network')
if __name__ == '__main__': cli()
