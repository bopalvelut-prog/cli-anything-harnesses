import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def install(): subprocess.run(['poetry', 'install'])
@cli.command()
def shell(): subprocess.run(['poetry', 'shell'])
@cli.command()
@click.argument('script')
def run(script): subprocess.run(['poetry', 'run', script])
@cli.command()
@click.argument('dep')
def add(dep): subprocess.run(['poetry', 'add', dep])
if __name__ == '__main__': cli()
