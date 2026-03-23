import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('presentation running')
@cli.command()
def start(): click.echo('presentation started')
if __name__ == '__main__': cli()
