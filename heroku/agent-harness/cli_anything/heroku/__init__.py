import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def login(): subprocess.run(['heroku', 'login'])
@cli.command()
def deploy(): subprocess.run(['git', 'push', 'heroku', 'main'])
@cli.command()
def logs(): subprocess.run(['heroku', 'logs', '--tail'])
@cli.command()
def ps(): subprocess.run(['heroku', 'ps'])
if __name__ == '__main__': cli()
