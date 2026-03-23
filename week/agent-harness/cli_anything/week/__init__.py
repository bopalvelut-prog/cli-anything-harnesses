import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('week running')
@cli.command()
def start(): click.echo('week started')
if __name__ == '__main__': cli()
