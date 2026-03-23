import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('pre running')
@cli.command()
def start(): click.echo('pre started')
if __name__ == '__main__': cli()
