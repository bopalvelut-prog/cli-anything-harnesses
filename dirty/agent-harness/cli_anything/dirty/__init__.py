import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('dirty running')
@cli.command()
def start(): click.echo('dirty started')
if __name__ == '__main__': cli()
