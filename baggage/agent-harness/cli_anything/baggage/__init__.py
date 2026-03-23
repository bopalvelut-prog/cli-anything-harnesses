import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('baggage running')
@cli.command()
def start(): click.echo('baggage started')
if __name__ == '__main__': cli()
