import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('mockserver running')
@cli.command()
def start(): click.echo('mockserver started')
if __name__ == '__main__': cli()
