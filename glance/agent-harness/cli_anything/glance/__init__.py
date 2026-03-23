import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('glance running')
@cli.command()
def start(): click.echo('glance started')
if __name__ == '__main__': cli()
