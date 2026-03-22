import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def summary(): subprocess.run(['du', '-sh', '.'])
@cli.command()
def all(): subprocess.run(['du', '-h', '.'])
if __name__ == '__main__': cli()
