import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('bake running')
@cli.command()
def start(): click.echo('bake started')
if __name__ == '__main__': cli()
