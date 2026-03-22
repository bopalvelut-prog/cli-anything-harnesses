import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def signin(): subprocess.run(['op', 'signin'])
@cli.command()
def list(): subprocess.run(['op', 'item', 'list'])
if __name__ == '__main__': cli()
