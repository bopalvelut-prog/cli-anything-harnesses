import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('tooth running')
@cli.command()
def start(): click.echo('tooth started')
if __name__ == '__main__': cli()
