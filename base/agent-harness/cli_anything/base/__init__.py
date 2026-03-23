import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('base running')
@cli.command()
def start(): click.echo('base started')
if __name__ == '__main__': cli()
