import click, subprocess
@click.group()
def cli(): pass
@cli.command()
@click.argument('name')
def new(name): subprocess.run(['screen', '-S', name])
@cli.command()
def list(): subprocess.run(['screen', '-ls'])
@cli.command()
def attach(): subprocess.run(['screen', '-r'])
if __name__ == '__main__': cli()
