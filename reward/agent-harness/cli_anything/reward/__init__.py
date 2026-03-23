import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('reward running')
@cli.command()
def start(): click.echo('reward started')
if __name__ == '__main__': cli()
