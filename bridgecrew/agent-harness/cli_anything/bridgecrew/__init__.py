import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def scan(): subprocess.run(['bridgecrew', '-d', '.'])
@cli.command()
def fix(): click.echo('Bridgecrew fix')
if __name__ == '__main__': cli()
