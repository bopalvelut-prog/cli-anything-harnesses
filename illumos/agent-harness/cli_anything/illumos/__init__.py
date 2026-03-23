import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('illumos running')
@cli.command()
def start(): click.echo('illumos started')
if __name__ == '__main__': cli()
