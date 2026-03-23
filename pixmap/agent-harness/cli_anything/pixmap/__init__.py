import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('pixmap running')
@cli.command()
def start(): click.echo('pixmap started')
if __name__ == '__main__': cli()
