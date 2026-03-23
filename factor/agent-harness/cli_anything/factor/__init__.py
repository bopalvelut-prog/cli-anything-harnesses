import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('factor running')
@cli.command()
def start(): click.echo('factor started')
if __name__ == '__main__': cli()
