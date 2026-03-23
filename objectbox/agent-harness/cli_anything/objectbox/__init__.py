import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('objectbox running')
@cli.command()
def start(): click.echo('objectbox started')
if __name__ == '__main__': cli()
