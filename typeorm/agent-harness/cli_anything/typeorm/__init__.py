import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def migrate(): subprocess.run(['typeorm', 'migration:run'])
@cli.command()
def generate(): subprocess.run(['typeorm', 'migration:generate'])
if __name__ == '__main__': cli()
