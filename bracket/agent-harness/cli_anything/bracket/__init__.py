import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('bracket running')
@cli.command()
def start(): click.echo('bracket started')
if __name__ == '__main__': cli()
