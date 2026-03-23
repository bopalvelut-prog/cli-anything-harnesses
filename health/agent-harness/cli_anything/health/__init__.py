import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('health running')
@cli.command()
def start(): click.echo('health started')
if __name__ == '__main__': cli()
