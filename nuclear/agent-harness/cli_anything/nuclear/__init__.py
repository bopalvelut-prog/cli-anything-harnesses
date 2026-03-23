import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('nuclear running')
@cli.command()
def start(): click.echo('nuclear started')
if __name__ == '__main__': cli()
