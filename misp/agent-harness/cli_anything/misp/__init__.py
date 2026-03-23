import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('misp running')
@cli.command()
def start(): click.echo('misp started')
if __name__ == '__main__': cli()
