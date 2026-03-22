import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def login(): subprocess.run(['contentful', 'login'])
@cli.command()
def space(): subprocess.run(['contentful', 'space', 'list'])
if __name__ == '__main__': cli()
