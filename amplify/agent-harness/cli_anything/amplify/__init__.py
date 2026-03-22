import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def init(): subprocess.run(['amplify', 'init'])
@cli.command()
def push(): subprocess.run(['amplify', 'push'])
@cli.command()
def status(): subprocess.run(['amplify', 'status'])
@cli.command()
def publish(): subprocess.run(['amplify', 'publish'])
if __name__ == '__main__': cli()
