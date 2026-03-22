import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('ownCloud running')
@cli.command()
def files(): click.echo('ownCloud files')
if __name__ == '__main__': cli()
