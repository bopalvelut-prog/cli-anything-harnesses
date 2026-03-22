import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def build(): subprocess.run(['cargo', 'build'])
@cli.command()
def test(): subprocess.run(['cargo', 'test'])
@cli.command()
def run(): subprocess.run(['cargo', 'run'])
@cli.command()
@click.argument('name')
def new(name): subprocess.run(['cargo', 'new', name])
if __name__ == '__main__': cli()
