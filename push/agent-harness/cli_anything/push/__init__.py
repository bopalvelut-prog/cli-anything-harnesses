import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('push running')
@cli.command()
def start(): click.echo('push started')
if __name__ == '__main__': cli()
