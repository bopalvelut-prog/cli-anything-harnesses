import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('pure running')
@cli.command()
def start(): click.echo('pure started')
if __name__ == '__main__': cli()
