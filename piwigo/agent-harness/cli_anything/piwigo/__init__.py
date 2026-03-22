import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('Piwigo status')
@cli.command()
def albums(): click.echo('Piwigo albums')
if __name__ == '__main__': cli()
