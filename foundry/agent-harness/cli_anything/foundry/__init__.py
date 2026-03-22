import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def build(): subprocess.run(['forge', 'build'])
@cli.command()
def test(): subprocess.run(['forge', 'test'])
@cli.command()
def deploy(): subprocess.run(['forge', 'create'])
if __name__ == '__main__': cli()
