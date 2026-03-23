import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('result running')
@cli.command()
def start(): click.echo('result started')
if __name__ == '__main__': cli()
