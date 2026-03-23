import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('device running')
@cli.command()
def start(): click.echo('device started')
if __name__ == '__main__': cli()
