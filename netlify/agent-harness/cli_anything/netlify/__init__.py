import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def dev(): subprocess.run(['netlify', 'dev'])
@cli.command()
def deploy(): subprocess.run(['netlify', 'deploy', '--prod'])
@cli.command()
def status(): subprocess.run(['netlify', 'status'])
@cli.command()
def functions(): subprocess.run(['netlify', 'functions:list'])
if __name__ == '__main__': cli()
