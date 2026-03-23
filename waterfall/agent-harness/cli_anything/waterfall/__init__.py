import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('waterfall running')
@cli.command()
def start(): click.echo('waterfall started')
if __name__ == '__main__': cli()
