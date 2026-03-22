import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def install(): subprocess.run(['bun', 'install'])
@cli.command()
@click.argument('file')
def run(file): subprocess.run(['bun', 'run', file])
@cli.command()
def test(): subprocess.run(['bun', 'test'])
if __name__ == '__main__': cli()
