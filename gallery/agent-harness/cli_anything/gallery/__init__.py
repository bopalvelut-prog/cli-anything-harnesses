import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('Gallery status')
@cli.command()
def albums(): click.echo('Gallery albums')
if __name__ == '__main__': cli()
