import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def start(): subprocess.run(['npm', 'run', 'start'])
@cli.command()
def build(): subprocess.run(['npm', 'run', 'build'])
@cli.command()
def deploy(): subprocess.run(['npm', 'run', 'deploy'])
if __name__ == '__main__': cli()
