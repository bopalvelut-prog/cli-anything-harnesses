import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('secrets running')
@cli.command()
def start(): click.echo('secrets started')
if __name__ == '__main__': cli()
