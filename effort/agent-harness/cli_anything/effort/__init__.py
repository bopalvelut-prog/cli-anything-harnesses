import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('effort running')
@cli.command()
def start(): click.echo('effort started')
if __name__ == '__main__': cli()
