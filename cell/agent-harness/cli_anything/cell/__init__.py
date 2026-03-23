import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('cell running')
@cli.command()
def start(): click.echo('cell started')
if __name__ == '__main__': cli()
