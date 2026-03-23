import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('scene running')
@cli.command()
def start(): click.echo('scene started')
if __name__ == '__main__': cli()
