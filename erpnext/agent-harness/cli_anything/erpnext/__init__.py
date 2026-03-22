import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def start(): subprocess.run(['bench', 'start'])
@cli.command()
def migrate(): subprocess.run(['bench', 'migrate'])
if __name__ == '__main__': cli()
