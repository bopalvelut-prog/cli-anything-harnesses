import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('steer running')
@cli.command()
def start(): click.echo('steer started')
if __name__ == '__main__': cli()
