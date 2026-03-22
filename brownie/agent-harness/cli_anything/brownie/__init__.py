import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def compile(): subprocess.run(['brownie', 'compile'])
@cli.command()
def test(): subprocess.run(['brownie', 'test'])
@cli.command()
def run(): subprocess.run(['brownie', 'run'])
if __name__ == '__main__': cli()
