import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('genre running')
@cli.command()
def start(): click.echo('genre started')
if __name__ == '__main__': cli()
