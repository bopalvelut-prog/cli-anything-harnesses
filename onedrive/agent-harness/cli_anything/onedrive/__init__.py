import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('OneDrive status')
@cli.command()
def files(): click.echo('OneDrive files')
if __name__ == '__main__': cli()
