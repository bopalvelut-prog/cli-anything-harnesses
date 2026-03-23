import click
@click.group()
def cli(): pass
@cli.command()
def ls(): click.echo('Storage ls')
@cli.command()
def cp(): click.echo('Storage cp')
if __name__ == '__main__': cli()
