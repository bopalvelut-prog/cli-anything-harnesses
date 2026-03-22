import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def monitor(): subprocess.run(['iftop'])
if __name__ == '__main__': cli()
