import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('pCloud status')
@cli.command()
def files(): click.echo('pCloud files')
if __name__ == '__main__': cli()
