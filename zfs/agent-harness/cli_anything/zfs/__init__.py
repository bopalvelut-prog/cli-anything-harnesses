import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): subprocess.run(['zpool', 'status'])
@cli.command()
def list(): subprocess.run(['zfs', 'list'])
if __name__ == '__main__': cli()
