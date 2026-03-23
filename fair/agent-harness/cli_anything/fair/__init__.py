import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('fair running')
@cli.command()
def start(): click.echo('fair started')
if __name__ == '__main__': cli()
