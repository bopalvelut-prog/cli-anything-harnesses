import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('path running')
@cli.command()
def start(): click.echo('path started')
if __name__ == '__main__': cli()
