import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('Dropbox status')
@cli.command()
def files(): click.echo('Dropbox files')
if __name__ == '__main__': cli()
