import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def up(): subprocess.run(['railway', 'up'])
@cli.command()
def status(): subprocess.run(['railway', 'status'])
@cli.command()
def logs(): subprocess.run(['railway', 'logs'])
@cli.command()
def connect(): subprocess.run(['railway', 'connect'])
if __name__ == '__main__': cli()
