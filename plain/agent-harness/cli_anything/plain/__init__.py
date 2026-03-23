import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('plain running')
@cli.command()
def start(): click.echo('plain started')
if __name__ == '__main__': cli()
