import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('control running')
@cli.command()
def start(): click.echo('control started')
if __name__ == '__main__': cli()
