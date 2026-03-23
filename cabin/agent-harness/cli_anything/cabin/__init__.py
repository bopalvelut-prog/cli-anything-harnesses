import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('cabin running')
@cli.command()
def start(): click.echo('cabin started')
if __name__ == '__main__': cli()
