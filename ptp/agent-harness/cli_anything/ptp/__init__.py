import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('ptp running')
@cli.command()
def start(): click.echo('ptp started')
if __name__ == '__main__': cli()
