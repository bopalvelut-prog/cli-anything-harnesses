import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('supporter running')
@cli.command()
def start(): click.echo('supporter started')
if __name__ == '__main__': cli()
