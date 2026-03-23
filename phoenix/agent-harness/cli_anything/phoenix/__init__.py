import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('phoenix running')
@cli.command()
def start(): click.echo('phoenix started')
if __name__ == '__main__': cli()
