import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('wasp running')
@cli.command()
def start(): click.echo('wasp started')
if __name__ == '__main__': cli()
