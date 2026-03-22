import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def scan(): subprocess.run(['kics', 'scan', '-p', '.'])
if __name__ == '__main__': cli()
