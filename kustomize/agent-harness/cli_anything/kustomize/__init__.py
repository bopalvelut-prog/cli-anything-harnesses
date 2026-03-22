import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def build(): subprocess.run(['kustomize', 'build', '.'])
@cli.command()
def apply(): subprocess.run(['kustomize', 'build', '.', '|', 'kubectl', 'apply', '-f', '-'], shell=True)
if __name__ == '__main__': cli()
