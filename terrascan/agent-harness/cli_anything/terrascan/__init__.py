import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def scan(): subprocess.run(['terrascan', 'scan'])
@cli.command()
def init(): subprocess.run(['terrascan', 'init'])
if __name__ == '__main__': cli()
