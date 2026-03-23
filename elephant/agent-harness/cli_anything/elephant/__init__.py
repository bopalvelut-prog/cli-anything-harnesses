import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('elephant running')
@cli.command()
def start(): click.echo('elephant started')
if __name__ == '__main__': cli()
