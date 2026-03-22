import click, subprocess
@click.group()
def cli(): pass
@cli.command()
@click.argument('file')
def run(file): subprocess.run(['dart', 'run', file])
@cli.command()
def test(): subprocess.run(['dart', 'test'])
@cli.command()
def format(): subprocess.run(['dart', 'format', '.'])
if __name__ == '__main__': cli()
