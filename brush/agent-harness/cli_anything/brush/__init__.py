import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('brush running')
@cli.command()
def start(): click.echo('brush started')
if __name__ == '__main__': cli()
