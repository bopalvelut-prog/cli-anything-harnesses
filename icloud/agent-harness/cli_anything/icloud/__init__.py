import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('iCloud status')
@cli.command()
def files(): click.echo('iCloud files')
if __name__ == '__main__': cli()
