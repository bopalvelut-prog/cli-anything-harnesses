import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('kick running')
@cli.command()
def start(): click.echo('kick started')
if __name__ == '__main__': cli()
