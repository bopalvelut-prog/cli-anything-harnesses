import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('cloudinary running')
@cli.command()
def start(): click.echo('cloudinary started')
if __name__ == '__main__': cli()
