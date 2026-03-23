import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('satellite running')
@cli.command()
def start(): click.echo('satellite started')
if __name__ == '__main__': cli()
