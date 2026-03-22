import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def login(): click.echo('Dashlane login')
@cli.command()
def list(): click.echo('Dashlane entries')
if __name__ == '__main__': cli()
