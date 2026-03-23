import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('hp running')
@cli.command()
def start(): click.echo('hp started')
if __name__ == '__main__': cli()
