import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def list(): subprocess.run(['lsblk'])
@cli.command()
def all(): subprocess.run(['lsblk', '-a'])
if __name__ == '__main__': cli()
