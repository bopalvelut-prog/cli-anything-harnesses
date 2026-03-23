import click
@click.group()
def cli(): pass
@cli.command()
def ls(): click.echo('Spaces ls')
@cli.command()
def cp(): click.echo('Spaces cp')
if __name__ == '__main__': cli()
