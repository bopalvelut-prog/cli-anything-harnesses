import click, subprocess
@click.group()
def cli(): pass
@cli.command()
@click.argument('path')
def backup(path): subprocess.run(['restic', 'backup', path])
@cli.command()
@click.argument('snapshot')
def restore(snapshot): subprocess.run(['restic', 'restore', snapshot])
@cli.command()
def snapshots(): subprocess.run(['restic', 'snapshots'])
@cli.command()
def check(): subprocess.run(['restic', 'check'])
if __name__ == '__main__': cli()
