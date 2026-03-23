import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('genuine running')
@cli.command()
def start(): click.echo('genuine started')
if __name__ == '__main__': cli()
