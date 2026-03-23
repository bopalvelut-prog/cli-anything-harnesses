import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('xquery running')
@cli.command()
def start(): click.echo('xquery started')
if __name__ == '__main__': cli()
