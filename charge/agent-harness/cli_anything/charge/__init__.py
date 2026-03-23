import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('charge running')
@cli.command()
def start(): click.echo('charge started')
if __name__ == '__main__': cli()
