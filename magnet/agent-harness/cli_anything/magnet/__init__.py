import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('magnet running')
@cli.command()
def start(): click.echo('magnet started')
if __name__ == '__main__': cli()
