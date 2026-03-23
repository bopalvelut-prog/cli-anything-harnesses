import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('now running')
@cli.command()
def start(): click.echo('now started')
if __name__ == '__main__': cli()
