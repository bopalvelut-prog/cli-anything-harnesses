import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('PhotoPrism status')
@cli.command()
def albums(): click.echo('PhotoPrism albums')
if __name__ == '__main__': cli()
