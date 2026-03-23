import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('lifx running')
@cli.command()
def start(): click.echo('lifx started')
if __name__ == '__main__': cli()
