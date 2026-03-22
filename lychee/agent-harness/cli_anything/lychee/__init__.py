import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('Lychee status')
@cli.command()
def albums(): click.echo('Lychee albums')
if __name__ == '__main__': cli()
