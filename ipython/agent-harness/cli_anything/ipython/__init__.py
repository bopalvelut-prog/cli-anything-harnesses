import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('ipython running')
@cli.command()
def start(): click.echo('ipython started')
if __name__ == '__main__': cli()
