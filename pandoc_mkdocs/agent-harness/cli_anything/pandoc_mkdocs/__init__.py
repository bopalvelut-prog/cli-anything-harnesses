import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def serve(): subprocess.run(['mkdocs', 'serve'])
@cli.command()
def build(): subprocess.run(['mkdocs', 'build'])
@cli.command()
def deploy(): subprocess.run(['mkdocs', 'gh-deploy'])
if __name__ == '__main__': cli()
