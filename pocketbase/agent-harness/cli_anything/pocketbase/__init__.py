import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def serve(): subprocess.run(['pocketbase', 'serve'])
@cli.command()
def migrate(): subprocess.run(['pocketbase', 'migrate', 'up'])
if __name__ == '__main__': cli()
