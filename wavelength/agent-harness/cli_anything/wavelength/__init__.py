import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('wavelength running')
@cli.command()
def start(): click.echo('wavelength started')
if __name__ == '__main__': cli()
