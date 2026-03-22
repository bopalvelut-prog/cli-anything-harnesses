import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def build(): subprocess.run(['sphinx-build', '-b', 'html', 'source', 'build'])
@cli.command()
def clean(): subprocess.run(['sphinx-build', '-b', 'clean', 'source', 'build'])
@cli.command()
def livehtml(): subprocess.run(['sphinx-autobuild', 'source', 'build/html'])
if __name__ == '__main__': cli()
