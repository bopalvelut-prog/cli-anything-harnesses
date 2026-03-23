import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('pylint running')
@cli.command()
def start(): click.echo('pylint started')
if __name__ == '__main__': cli()
