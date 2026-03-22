import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def detect(): subprocess.run(['gphoto2', '--auto-detect'])
@cli.command()
def capture(): subprocess.run(['gphoto2', '--capture-image'])
@cli.command()
def download(): subprocess.run(['gphoto2', '--get-all-files'])
@cli.command()
def preview(): subprocess.run(['gphoto2', '--capture-preview'])
if __name__ == '__main__': cli()
