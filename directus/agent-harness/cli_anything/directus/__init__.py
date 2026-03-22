import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def start(): subprocess.run(['npx', 'directus', 'start'])
@cli.command()
def bootstrap(): subprocess.run(['npx', 'directus', 'bootstrap'])
if __name__ == '__main__': cli()
