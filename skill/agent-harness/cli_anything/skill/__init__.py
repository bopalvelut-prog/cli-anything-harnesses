import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('skill running')
@cli.command()
def start(): click.echo('skill started')
if __name__ == '__main__': cli()
