import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('conftest running')
@cli.command()
def start(): click.echo('conftest started')
if __name__ == '__main__': cli()
