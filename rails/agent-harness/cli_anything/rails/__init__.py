import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def server(): subprocess.run(['rails', 'server'])
@cli.command()
def console(): subprocess.run(['rails', 'console'])
if __name__ == '__main__': cli()
