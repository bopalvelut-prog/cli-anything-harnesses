import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('full running')
@cli.command()
def start(): click.echo('full started')
if __name__ == '__main__': cli()
