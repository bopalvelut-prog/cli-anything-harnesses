import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def init(): subprocess.run(['dvc', 'init'])
@cli.command()
def add(): subprocess.run(['dvc', 'add'])
@cli.command()
def push(): subprocess.run(['dvc', 'push'])
if __name__ == '__main__': cli()
