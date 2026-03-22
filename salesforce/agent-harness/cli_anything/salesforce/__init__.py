import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def login(): subprocess.run(['sf', 'org', 'login', 'web'])
@cli.command()
def query(): subprocess.run(['sf', 'data', 'query'])
if __name__ == '__main__': cli()
