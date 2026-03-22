import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def init(): subprocess.run(['terraform', 'init'])
@cli.command()
def plan(): subprocess.run(['terraform', 'plan'])
@cli.command()
def apply(): subprocess.run(['terraform', 'apply'])
@cli.command()
def destroy(): subprocess.run(['terraform', 'destroy'])
if __name__ == '__main__': cli()
