import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('passion running')
@cli.command()
def start(): click.echo('passion started')
if __name__ == '__main__': cli()
