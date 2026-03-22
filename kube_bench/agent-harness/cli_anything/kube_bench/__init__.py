import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def check(): subprocess.run(['kube-bench'])
@cli.command()
def run(): subprocess.run(['kube-bench', 'run'])
if __name__ == '__main__': cli()
