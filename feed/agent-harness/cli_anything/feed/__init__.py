import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('feed running')
@cli.command()
def start(): click.echo('feed started')
if __name__ == '__main__': cli()
