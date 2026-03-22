import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def run(): subprocess.run(['flask', 'run'])
@cli.command()
def shell(): subprocess.run(['flask', 'shell'])
if __name__ == '__main__': cli()
