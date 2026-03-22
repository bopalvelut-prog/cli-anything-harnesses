import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def login(): subprocess.run(['terraform', 'login'])
@cli.command()
def workspace(): subprocess.run(['terraform', 'workspace', 'list'])
@cli.command()
def push(): subprocess.run(['terraform', 'push'])
if __name__ == '__main__': cli()
