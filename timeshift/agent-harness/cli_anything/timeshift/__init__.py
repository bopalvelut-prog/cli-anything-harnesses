import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def create(): subprocess.run(['timeshift', '--create', '--yes'])
@cli.command()
def list(): subprocess.run(['timeshift', '--list'])
@cli.command()
@click.argument('snapshot')
def restore(snapshot): subprocess.run(['timeshift', '--restore', '--snapshot', snapshot])
if __name__ == '__main__': cli()
