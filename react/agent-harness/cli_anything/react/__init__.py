import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def start(): subprocess.run(['npm', 'start'])
@cli.command()
def build(): subprocess.run(['npm', 'run', 'build'])
@cli.command()
def test(): subprocess.run(['npm', 'test'])
@cli.command()
def eject(): subprocess.run(['npm', 'run', 'eject'])
if __name__ == '__main__': cli()
