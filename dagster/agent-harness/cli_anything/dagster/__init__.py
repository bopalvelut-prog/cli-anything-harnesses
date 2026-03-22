import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def run(): subprocess.run(['dagster', 'dev'])
@cli.command()
def list(): subprocess.run(['dagster', 'pipeline', 'list'])
if __name__ == '__main__': cli()
