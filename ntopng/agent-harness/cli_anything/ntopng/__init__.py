import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('ntopng running')
@cli.command()
def start(): click.echo('ntopng started')
if __name__ == '__main__': cli()
