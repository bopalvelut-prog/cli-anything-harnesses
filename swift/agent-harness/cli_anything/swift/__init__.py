import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def run(): subprocess.run(['swift', 'run'])
@cli.command()
def build(): subprocess.run(['swift', 'build'])
@cli.command()
def test(): subprocess.run(['swift', 'test'])
if __name__ == '__main__': cli()
