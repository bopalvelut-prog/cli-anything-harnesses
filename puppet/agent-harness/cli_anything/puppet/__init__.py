import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def apply(): subprocess.run(['puppet', 'apply', 'site.pp'])
@cli.command()
def agent(): subprocess.run(['puppet', 'agent', '-t'])
if __name__ == '__main__': cli()
