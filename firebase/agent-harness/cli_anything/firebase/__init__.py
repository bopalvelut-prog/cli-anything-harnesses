import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def deploy(): subprocess.run(['firebase', 'deploy'])
@cli.command()
def emulators(): subprocess.run(['firebase', 'emulators:start'])
@cli.command()
def serve(): subprocess.run(['firebase', 'serve'])
@cli.command()
def functions(): subprocess.run(['firebase', 'functions:shell'])
if __name__ == '__main__': cli()
