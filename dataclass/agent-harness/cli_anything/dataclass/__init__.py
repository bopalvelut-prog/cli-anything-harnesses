import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('dataclass running')
@cli.command()
def start(): click.echo('dataclass started')
if __name__ == '__main__': cli()
