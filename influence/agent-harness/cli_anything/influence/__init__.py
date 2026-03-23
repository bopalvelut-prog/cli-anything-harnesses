import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('influence running')
@cli.command()
def start(): click.echo('influence started')
if __name__ == '__main__': cli()
