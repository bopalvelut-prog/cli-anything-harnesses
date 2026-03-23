import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('reduce running')
@cli.command()
def start(): click.echo('reduce started')
if __name__ == '__main__': cli()
