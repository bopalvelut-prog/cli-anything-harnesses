import click, subprocess
@click.group()
def cli(): pass
@cli.command()
@click.argument('name')
def get(name): subprocess.run(['pass', name])
@cli.command()
@click.argument('name')
def insert(name): subprocess.run(['pass', 'insert', name])
@cli.command()
def list(): subprocess.run(['pass', 'ls'])
if __name__ == '__main__': cli()
