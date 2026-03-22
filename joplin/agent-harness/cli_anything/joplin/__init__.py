import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def sync(): subprocess.run(['joplin', 'sync'])
@cli.command()
def notes(): subprocess.run(['joplin', 'ls'])
if __name__ == '__main__': cli()
