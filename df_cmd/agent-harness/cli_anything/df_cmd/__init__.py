import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def disk(): subprocess.run(['df', '-h'])
@cli.command()
def inode(): subprocess.run(['df', '-i'])
if __name__ == '__main__': cli()
