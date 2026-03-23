import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('paho running')
@cli.command()
def start(): click.echo('paho started')
if __name__ == '__main__': cli()
