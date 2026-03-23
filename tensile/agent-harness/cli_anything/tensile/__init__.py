import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('tensile running')
@cli.command()
def start(): click.echo('tensile started')
if __name__ == '__main__': cli()
