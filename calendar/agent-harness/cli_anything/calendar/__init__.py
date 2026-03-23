import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('calendar running')
@cli.command()
def start(): click.echo('calendar started')
if __name__ == '__main__': cli()
