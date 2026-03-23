import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('glass running')
@cli.command()
def start(): click.echo('glass started')
if __name__ == '__main__': cli()
