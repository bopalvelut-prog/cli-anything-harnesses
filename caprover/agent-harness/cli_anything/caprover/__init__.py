import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def login(): subprocess.run(['caprover', 'login'])
@cli.command()
def deploy(): subprocess.run(['caprover', 'deploy'])
@cli.command()
def status(): subprocess.run(['caprover', 'status'])
if __name__ == '__main__': cli()
