import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def serve(): subprocess.run(['ng', 'serve'])
@cli.command()
def build(): subprocess.run(['ng', 'build'])
@cli.command()
def test(): subprocess.run(['ng', 'test'])
@cli.command()
def generate(): subprocess.run(['ng', 'generate', 'component', 'my-component'])
if __name__ == '__main__': cli()
