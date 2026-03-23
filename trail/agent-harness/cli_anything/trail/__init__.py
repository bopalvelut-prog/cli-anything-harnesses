import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('trail running')
@cli.command()
def start(): click.echo('trail started')
if __name__ == '__main__': cli()
