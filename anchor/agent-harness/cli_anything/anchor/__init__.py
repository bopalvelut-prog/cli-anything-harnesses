import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def build(): subprocess.run(['anchor', 'build'])
@cli.command()
def test(): subprocess.run(['anchor', 'test'])
@cli.command()
def deploy(): subprocess.run(['anchor', 'deploy'])
if __name__ == '__main__': cli()
