import click
@click.group()
def cli(): pass
@cli.command()
def ls(): click.echo('Blob ls')
@cli.command()
def cp(): click.echo('Blob cp')
if __name__ == '__main__': cli()
