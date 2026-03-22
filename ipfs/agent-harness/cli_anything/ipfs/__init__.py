import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def init(): subprocess.run(['ipfs', 'init'])
@cli.command()
def add(): subprocess.run(['ipfs', 'add'])
@cli.command()
def cat(): subprocess.run(['ipfs', 'cat'])
@cli.command()
def peers(): subprocess.run(['ipfs', 'swarm', 'peers'])
if __name__ == '__main__': cli()
