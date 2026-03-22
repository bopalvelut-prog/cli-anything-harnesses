import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def info(): subprocess.run(['xfs_info', '/'])
@cli.command()
def repair(): subprocess.run(['xfs_repair', '-n', '/dev/sda1'])
if __name__ == '__main__': cli()
