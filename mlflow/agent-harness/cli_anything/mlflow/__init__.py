import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def ui(): subprocess.run(['mlflow', 'ui'])
@cli.command()
def run(): subprocess.run(['mlflow', 'run'])
if __name__ == '__main__': cli()
