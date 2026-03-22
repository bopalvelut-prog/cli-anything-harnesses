import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def scan(): subprocess.run(['clamscan', '-r', '.'])
@cli.command()
def update(): subprocess.run(['freshclam'])
if __name__ == '__main__': cli()
