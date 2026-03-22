import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def start(): subprocess.run(['nest', 'start'])
@cli.command()
def build(): subprocess.run(['nest', 'build'])
if __name__ == '__main__': cli()
