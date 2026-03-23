import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('employ running')
@cli.command()
def start(): click.echo('employ started')
if __name__ == '__main__': cli()
