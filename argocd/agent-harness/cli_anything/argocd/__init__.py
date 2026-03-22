import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def login(): subprocess.run(['argocd', 'login'])
@cli.command()
def sync(): subprocess.run(['argocd', 'app', 'sync'])
@cli.command()
def list(): subprocess.run(['argocd', 'app', 'list'])
@cli.command()
def diff(): subprocess.run(['argocd', 'app', 'diff'])
if __name__ == '__main__': cli()
