import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def dev(): subprocess.run(['next', 'dev'])
@cli.command()
def build(): subprocess.run(['next', 'build'])
@cli.command()
def start(): subprocess.run(['next', 'start'])
@cli.command()
def lint(): subprocess.run(['next', 'lint'])
if __name__ == '__main__': cli()
