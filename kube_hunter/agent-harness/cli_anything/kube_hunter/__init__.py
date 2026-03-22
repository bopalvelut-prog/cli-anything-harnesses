import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def scan(): subprocess.run(['kube-hunter'])
if __name__ == '__main__': cli()
