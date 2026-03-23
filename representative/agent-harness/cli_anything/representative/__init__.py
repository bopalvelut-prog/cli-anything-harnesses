import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('representative running')
@cli.command()
def start(): click.echo('representative started')
if __name__ == '__main__': cli()
