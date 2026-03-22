import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def scan(): subprocess.run(['checkov', '-d', '.'])
@cli.command()
def fix(): subprocess.run(['checkov', '-d', '.', '--fix'])
if __name__ == '__main__': cli()
