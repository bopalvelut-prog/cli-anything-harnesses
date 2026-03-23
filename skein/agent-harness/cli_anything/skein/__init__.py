import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('skein running')
@cli.command()
def start(): click.echo('skein started')
if __name__ == '__main__': cli()
