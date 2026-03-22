import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def start(): subprocess.run(['sanity', 'start'])
@cli.command()
def deploy(): subprocess.run(['sanity', 'deploy'])
if __name__ == '__main__': cli()
