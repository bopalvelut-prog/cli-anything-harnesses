import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('Chevereto status')
@cli.command()
def albums(): click.echo('Chevereto albums')
if __name__ == '__main__': cli()
