import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def build(): subprocess.run(['porter', 'build'])
@cli.command()
def install(): subprocess.run(['porter', 'install'])
@cli.command()
def upgrade(): subprocess.run(['porter', 'upgrade'])
if __name__ == '__main__': cli()
