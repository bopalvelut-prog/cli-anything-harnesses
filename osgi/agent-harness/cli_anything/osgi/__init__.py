import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('osgi running')
@cli.command()
def start(): click.echo('osgi started')
if __name__ == '__main__': cli()
