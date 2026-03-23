import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('incident running')
@cli.command()
def start(): click.echo('incident started')
if __name__ == '__main__': cli()
