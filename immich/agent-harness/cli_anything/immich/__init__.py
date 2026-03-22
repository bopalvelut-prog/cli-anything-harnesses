import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('Immich status')
@cli.command()
def albums(): click.echo('Immich albums')
if __name__ == '__main__': cli()
