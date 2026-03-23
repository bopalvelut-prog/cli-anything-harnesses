import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('autosar running')
@cli.command()
def start(): click.echo('autosar started')
if __name__ == '__main__': cli()
