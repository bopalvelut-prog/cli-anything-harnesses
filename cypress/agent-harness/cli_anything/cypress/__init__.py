import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def open(): subprocess.run(['cypress', 'open'])
@cli.command()
def run(): subprocess.run(['cypress', 'run'])
@cli.command()
def ci(): subprocess.run(['cypress', 'run', '--ci-build-id'])
if __name__ == '__main__': cli()
