import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('clipper running')
@cli.command()
def start(): click.echo('clipper started')
if __name__ == '__main__': cli()
