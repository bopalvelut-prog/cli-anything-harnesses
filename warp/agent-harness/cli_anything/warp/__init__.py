import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('warp running')
@cli.command()
def start(): click.echo('warp started')
if __name__ == '__main__': cli()
