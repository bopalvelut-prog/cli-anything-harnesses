import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('obspy running')
@cli.command()
def start(): click.echo('obspy started')
if __name__ == '__main__': cli()
