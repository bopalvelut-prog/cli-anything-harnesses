import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('apiman running')
@cli.command()
def start(): click.echo('apiman started')
if __name__ == '__main__': cli()
