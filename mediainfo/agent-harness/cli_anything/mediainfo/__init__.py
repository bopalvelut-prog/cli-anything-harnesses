import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('mediainfo running')
@cli.command()
def start(): click.echo('mediainfo started')
if __name__ == '__main__': cli()
