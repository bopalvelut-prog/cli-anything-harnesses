import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('doozer running')
@cli.command()
def start(): click.echo('doozer started')
if __name__ == '__main__': cli()
