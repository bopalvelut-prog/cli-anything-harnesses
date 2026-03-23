import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('bright running')
@cli.command()
def start(): click.echo('bright started')
if __name__ == '__main__': cli()
