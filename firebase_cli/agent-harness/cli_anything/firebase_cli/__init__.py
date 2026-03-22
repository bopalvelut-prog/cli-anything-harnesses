import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def init(): subprocess.run(['firebase', 'init'])
@cli.command()
def login(): subprocess.run(['firebase', 'login'])
if __name__ == '__main__': cli()
