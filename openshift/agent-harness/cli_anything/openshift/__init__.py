import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def login(): subprocess.run(['oc', 'login'])
@cli.command()
def projects(): subprocess.run(['oc', 'get', 'projects'])
@cli.command()
def new_app(): subprocess.run(['oc', 'new-app'])
if __name__ == '__main__': cli()
