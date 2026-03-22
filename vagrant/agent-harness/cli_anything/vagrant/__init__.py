import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def up(): subprocess.run(['vagrant', 'up'])
@cli.command()
def destroy(): subprocess.run(['vagrant', 'destroy', '-f'])
@cli.command()
def halt(): subprocess.run(['vagrant', 'halt'])
@cli.command()
def status(): subprocess.run(['vagrant', 'status'])
if __name__ == '__main__': cli()
