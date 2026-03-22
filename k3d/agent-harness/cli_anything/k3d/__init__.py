import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def create(): subprocess.run(['k3d', 'cluster', 'create'])
@cli.command()
def delete(): subprocess.run(['k3d', 'cluster', 'delete'])
@cli.command()
def list(): subprocess.run(['k3d', 'cluster', 'list'])
if __name__ == '__main__': cli()
