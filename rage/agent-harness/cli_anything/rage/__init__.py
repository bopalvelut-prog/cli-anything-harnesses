import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('rage running')
@cli.command()
def start(): click.echo('rage started')
if __name__ == '__main__': cli()
