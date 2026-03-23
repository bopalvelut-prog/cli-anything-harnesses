import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('flatpak running')
@cli.command()
def start(): click.echo('flatpak started')
if __name__ == '__main__': cli()
