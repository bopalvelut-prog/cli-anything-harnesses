import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('uncle running')
@cli.command()
def start(): click.echo('uncle started')
if __name__ == '__main__': cli()
