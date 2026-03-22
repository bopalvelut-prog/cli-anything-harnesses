import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def login(): subprocess.run(['bw', 'login'])
@cli.command()
def list(): subprocess.run(['bw', 'list', 'items'])
@cli.command()
def sync(): subprocess.run(['bw', 'sync'])
if __name__ == '__main__': cli()
