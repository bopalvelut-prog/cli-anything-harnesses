import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('sick running')
@cli.command()
def start(): click.echo('sick started')
if __name__ == '__main__': cli()
