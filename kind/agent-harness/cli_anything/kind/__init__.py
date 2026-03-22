import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def create(): subprocess.run(['kind', 'create', 'cluster'])
@cli.command()
def delete(): subprocess.run(['kind', 'delete', 'cluster'])
@cli.command()
def clusters(): subprocess.run(['kind', 'get', 'clusters'])
if __name__ == '__main__': cli()
