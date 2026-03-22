import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('LibrePhotos status')
@cli.command()
def albums(): click.echo('LibrePhotos albums')
if __name__ == '__main__': cli()
