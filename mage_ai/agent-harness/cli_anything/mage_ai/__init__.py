import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def start(): subprocess.run(['mage', 'start'])
@cli.command()
def run(): subprocess.run(['mage', 'run'])
if __name__ == '__main__': cli()
