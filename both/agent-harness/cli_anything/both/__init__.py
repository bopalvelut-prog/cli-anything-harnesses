import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('both running')
@cli.command()
def start(): click.echo('both started')
if __name__ == '__main__': cli()
