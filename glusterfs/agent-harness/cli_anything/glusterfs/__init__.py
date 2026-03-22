import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def info(): subprocess.run(['gluster', 'peer', 'status'])
@cli.command()
def volumes(): subprocess.run(['gluster', 'volume', 'info'])
if __name__ == '__main__': cli()
