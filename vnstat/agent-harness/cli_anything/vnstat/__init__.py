import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): subprocess.run(['vnstat', '-l'])
@cli.command()
def summary(): subprocess.run(['vnstat', '-s'])
if __name__ == '__main__': cli()
