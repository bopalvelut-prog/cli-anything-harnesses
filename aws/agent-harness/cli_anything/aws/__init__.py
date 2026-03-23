import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('aws running')
@cli.command()
def start(): click.echo('aws started')
if __name__ == '__main__': cli()
