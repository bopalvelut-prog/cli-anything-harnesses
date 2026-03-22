import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def compile(): subprocess.run(['g++', '-o', 'main', 'main.cpp'])
@cli.command()
def run(): subprocess.run(['./main'])
@cli.command()
def cmake(): subprocess.run(['cmake', '.', '&&', 'make'], shell=True)
if __name__ == '__main__': cli()
