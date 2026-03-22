import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def dev(): subprocess.run(['vite'])
@cli.command()
def build(): subprocess.run(['vite', 'build'])
@cli.command()
def preview(): subprocess.run(['vite', 'preview'])
if __name__ == '__main__': cli()
