import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('cython running')
@cli.command()
def start(): click.echo('cython started')
if __name__ == '__main__': cli()
