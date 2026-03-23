import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('qdrant running')
@cli.command()
def start(): click.echo('qdrant started')
if __name__ == '__main__': cli()
