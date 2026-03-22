import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def new(): subprocess.run(['kedro', 'new'])
@cli.command()
def run(): subprocess.run(['kedro', 'run'])
if __name__ == '__main__': cli()
