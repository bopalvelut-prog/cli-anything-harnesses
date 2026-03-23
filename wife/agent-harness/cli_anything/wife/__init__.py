import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('wife running')
@cli.command()
def start(): click.echo('wife started')
if __name__ == '__main__': cli()
