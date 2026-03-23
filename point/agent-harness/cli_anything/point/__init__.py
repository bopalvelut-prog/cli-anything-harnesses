import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('point running')
@cli.command()
def start(): click.echo('point started')
if __name__ == '__main__': cli()
