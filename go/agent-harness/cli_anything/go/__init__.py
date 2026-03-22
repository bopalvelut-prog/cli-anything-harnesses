import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def build(): subprocess.run(['go', 'build'])
@cli.command()
def test(): subprocess.run(['go', 'test', './...'])
@cli.command()
def run(): subprocess.run(['go', 'run', '.'])
@cli.command()
@click.argument('mod')
def get(mod): subprocess.run(['go', 'get', mod])
if __name__ == '__main__': cli()
