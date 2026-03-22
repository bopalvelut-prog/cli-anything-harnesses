import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def install(): subprocess.run(['pipenv', 'install'])
@cli.command()
def shell(): subprocess.run(['pipenv', 'shell'])
@cli.command()
def lock(): subprocess.run(['pipenv', 'lock'])
@cli.command()
@click.argument('dep')
def add(dep): subprocess.run(['pipenv', 'install', dep])
if __name__ == '__main__': cli()
