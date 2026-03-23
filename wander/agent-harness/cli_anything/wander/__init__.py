import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('wander running')
@cli.command()
def start(): click.echo('wander started')
if __name__ == '__main__': cli()
