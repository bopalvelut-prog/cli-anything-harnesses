import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def lint(): subprocess.run(['eslint', '.'])
@cli.command()
def fix(): subprocess.run(['eslint', '.', '--fix'])
@cli.command()
@click.argument('file')
def check(file): subprocess.run(['eslint', file])
if __name__ == '__main__': cli()
