import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def start(): subprocess.run(['node', 'index.js'])
@cli.command()
def dev(): subprocess.run(['nodemon', 'index.js'])
if __name__ == '__main__': cli()
