import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('sound running')
@cli.command()
def start(): click.echo('sound started')
if __name__ == '__main__': cli()
