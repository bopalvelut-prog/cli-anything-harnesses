import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('buyer running')
@cli.command()
def start(): click.echo('buyer started')
if __name__ == '__main__': cli()
