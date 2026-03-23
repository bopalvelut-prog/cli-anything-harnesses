import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('angular_material running')
@cli.command()
def start(): click.echo('angular_material started')
if __name__ == '__main__': cli()
