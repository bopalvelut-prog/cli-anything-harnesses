import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('Transmission status')
@cli.command()
def download(): click.echo('Adding torrent')
if __name__ == '__main__': cli()
