import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('unable running')
@cli.command()
def start(): click.echo('unable started')
if __name__ == '__main__': cli()
