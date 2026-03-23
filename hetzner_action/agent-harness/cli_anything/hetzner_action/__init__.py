import click
@click.group()
def cli(): pass
@cli.command()
def list(): click.echo('Actions')
@cli.command()
def get(): click.echo('Get action')
if __name__ == '__main__': cli()
