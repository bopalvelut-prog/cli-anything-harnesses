import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('appdynamics running')
@cli.command()
def start(): click.echo('appdynamics started')
if __name__ == '__main__': cli()
