import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def login(): subprocess.run(['prismic', 'login'])
@cli.command()
def new(): subprocess.run(['prismic', 'sm', 'new'])
if __name__ == '__main__': cli()
