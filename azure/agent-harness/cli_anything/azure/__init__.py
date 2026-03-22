import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def login(): subprocess.run(['az', 'login'])
@cli.command()
def groups(): subprocess.run(['az', 'group', 'list'])
if __name__ == '__main__': cli()
