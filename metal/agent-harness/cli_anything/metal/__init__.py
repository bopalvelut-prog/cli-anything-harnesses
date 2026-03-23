import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('metal running')
@cli.command()
def start(): click.echo('metal started')
if __name__ == '__main__': cli()
