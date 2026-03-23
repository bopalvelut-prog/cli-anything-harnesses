import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('observe running')
@cli.command()
def start(): click.echo('observe started')
if __name__ == '__main__': cli()
