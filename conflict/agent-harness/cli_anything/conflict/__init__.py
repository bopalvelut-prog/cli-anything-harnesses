import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('conflict running')
@cli.command()
def start(): click.echo('conflict started')
if __name__ == '__main__': cli()
