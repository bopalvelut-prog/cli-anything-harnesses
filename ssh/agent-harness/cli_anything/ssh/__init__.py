import click, subprocess
@click.group()
def cli(): pass
@cli.command()
@click.argument('host')
def connect(host): subprocess.run(['ssh', host])
@cli.command()
@click.argument('file')
@click.argument('dest')
def copy(file, dest): subprocess.run(['scp', file, dest])
@cli.command()
def keys(): subprocess.run(['ls', '-la', '~/.ssh/'])
if __name__ == '__main__': cli()
