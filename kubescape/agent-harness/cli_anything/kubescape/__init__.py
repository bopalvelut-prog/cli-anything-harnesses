import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def scan(): subprocess.run(['kubescape', 'scan', '.'])
@cli.command()
def fix(): subprocess.run(['kubescape', 'fix', '.'])
if __name__ == '__main__': cli()
