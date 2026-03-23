import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('dumb running')
@cli.command()
def start(): click.echo('dumb started')
if __name__ == '__main__': cli()
