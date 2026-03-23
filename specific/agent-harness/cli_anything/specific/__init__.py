import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('specific running')
@cli.command()
def start(): click.echo('specific started')
if __name__ == '__main__': cli()
