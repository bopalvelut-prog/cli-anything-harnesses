import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def dev(): subprocess.run(['nuxi', 'dev'])
@cli.command()
def build(): subprocess.run(['nuxi', 'build'])
@cli.command()
def generate(): subprocess.run(['nuxi', 'generate'])
if __name__ == '__main__': cli()
