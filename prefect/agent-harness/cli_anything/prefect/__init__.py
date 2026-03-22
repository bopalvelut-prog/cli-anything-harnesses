import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def flows(): subprocess.run(['prefect', 'flow', 'ls'])
@cli.command()
def deploy(): subprocess.run(['prefect', 'deploy'])
if __name__ == '__main__': cli()
