import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def start(): subprocess.run(['minikube', 'start'])
@cli.command()
def stop(): subprocess.run(['minikube', 'stop'])
@cli.command()
def dashboard(): subprocess.run(['minikube', 'dashboard'])
if __name__ == '__main__': cli()
