import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('sky running')
@cli.command()
def start(): click.echo('sky started')
if __name__ == '__main__': cli()
