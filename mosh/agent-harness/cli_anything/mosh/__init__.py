import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('mosh running')
@cli.command()
def start(): click.echo('mosh started')
if __name__ == '__main__': cli()
