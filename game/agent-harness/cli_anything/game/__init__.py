import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('game running')
@cli.command()
def start(): click.echo('game started')
if __name__ == '__main__': cli()
