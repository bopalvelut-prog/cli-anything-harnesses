import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def analyze(): subprocess.run(['codeql', 'database', 'analyze', '.'])
@cli.command()
def create(): subprocess.run(['codeql', 'database', 'create', 'codeql-db'])
if __name__ == '__main__': cli()
