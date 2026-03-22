import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def tools(): click.echo('Security tools installed')
@cli.command()
def update(): subprocess.run(['apt-get', 'update'])
@cli.command()
def upgrade(): subprocess.run(['apt-get', 'upgrade', '-y'])
if __name__ == '__main__': cli()
