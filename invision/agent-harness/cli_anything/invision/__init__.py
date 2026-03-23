import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('invision running')
@cli.command()
def start(): click.echo('invision started')
if __name__ == '__main__': cli()
