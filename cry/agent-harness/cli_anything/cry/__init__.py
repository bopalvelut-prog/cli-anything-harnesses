import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('cry running')
@cli.command()
def start(): click.echo('cry started')
if __name__ == '__main__': cli()
