import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('orientation running')
@cli.command()
def start(): click.echo('orientation started')
if __name__ == '__main__': cli()
