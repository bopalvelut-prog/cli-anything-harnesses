import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('farm running')
@cli.command()
def start(): click.echo('farm started')
if __name__ == '__main__': cli()
