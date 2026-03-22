import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def top(): subprocess.run(['htop'])
@cli.command()
def ps(): subprocess.run(['ps', 'aux', '--sort=-%mem'])
if __name__ == '__main__': cli()
