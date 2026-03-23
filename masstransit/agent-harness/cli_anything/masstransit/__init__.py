import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('masstransit running')
@cli.command()
def start(): click.echo('masstransit started')
if __name__ == '__main__': cli()
