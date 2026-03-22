import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def dev(): subprocess.run(['payload', 'dev'])
@cli.command()
def build(): subprocess.run(['payload', 'build'])
if __name__ == '__main__': cli()
