import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('singleton running')
@cli.command()
def start(): click.echo('singleton started')
if __name__ == '__main__': cli()
