import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def get(): subprocess.run(['kubectl', 'get', 'pods'])
@cli.command()
def apply(): subprocess.run(['kubectl', 'apply', '-f', '.'])
@cli.command()
def describe(): subprocess.run(['kubectl', 'describe', 'nodes'])
if __name__ == '__main__': cli()
