import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def install(): subprocess.run(['linkerd', 'install'])
@cli.command()
def check(): subprocess.run(['linkerd', 'check'])
@cli.command()
def dashboard(): subprocess.run(['linkerd', 'dashboard'])
if __name__ == '__main__': cli()
