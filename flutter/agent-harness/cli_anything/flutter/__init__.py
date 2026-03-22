import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def run(): subprocess.run(['flutter', 'run'])
@cli.command()
def build(): subprocess.run(['flutter', 'build', 'apk'])
@cli.command()
def doctor(): subprocess.run(['flutter', 'doctor'])
@cli.command()
def create(): subprocess.run(['flutter', 'create', 'my_app'])
if __name__ == '__main__': cli()
