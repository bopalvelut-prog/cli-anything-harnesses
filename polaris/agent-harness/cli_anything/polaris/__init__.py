import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def audit(): subprocess.run(['polaris', 'audit'])
@cli.command()
def dashboard(): subprocess.run(['polaris', 'dashboard'])
if __name__ == '__main__': cli()
