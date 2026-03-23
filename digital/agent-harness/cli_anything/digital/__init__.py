import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('digital running')
@cli.command()
def start(): click.echo('digital started')
if __name__ == '__main__': cli()
