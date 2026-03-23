import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('visible running')
@cli.command()
def start(): click.echo('visible started')
if __name__ == '__main__': cli()
