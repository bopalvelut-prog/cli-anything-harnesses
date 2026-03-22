import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def install(): subprocess.run(['flux', 'install'])
@cli.command()
def status(): subprocess.run(['flux', 'get', 'all'])
@cli.command()
def reconcile(): subprocess.run(['flux', 'reconcile', 'all'])
if __name__ == '__main__': cli()
