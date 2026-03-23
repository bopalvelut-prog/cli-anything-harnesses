import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('perses running')
@cli.command()
def start(): click.echo('perses started')
if __name__ == '__main__': cli()
