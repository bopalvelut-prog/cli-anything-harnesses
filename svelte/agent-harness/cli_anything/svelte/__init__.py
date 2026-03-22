import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def dev(): subprocess.run(['npm', 'run', 'dev'])
@cli.command()
def build(): subprocess.run(['npm', 'run', 'build'])
@cli.command()
def preview(): subprocess.run(['npm', 'run', 'preview'])
if __name__ == '__main__': cli()
