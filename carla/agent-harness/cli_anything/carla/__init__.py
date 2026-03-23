import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('carla running')
@cli.command()
def start(): click.echo('carla started')
if __name__ == '__main__': cli()
