import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def install(): subprocess.run(['npm', 'install'])
@cli.command()
def test(): subprocess.run(['npm', 'test'])
@cli.command()
def start(): subprocess.run(['npm', 'start'])
@cli.command()
@click.argument('script')
def run(script): subprocess.run(['npm', 'run', script])
if __name__ == '__main__': cli()
