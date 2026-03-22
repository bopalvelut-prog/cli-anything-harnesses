import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def login(): subprocess.run(['gcloud', 'auth', 'login'])
@cli.command()
def projects(): subprocess.run(['gcloud', 'projects', 'list'])
if __name__ == '__main__': cli()
