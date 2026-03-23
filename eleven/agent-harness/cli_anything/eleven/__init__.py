import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('eleven running')
@cli.command()
def start(): click.echo('eleven started')
if __name__ == '__main__': cli()
