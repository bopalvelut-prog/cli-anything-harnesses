import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def update(): subprocess.run(['liquibase', 'update'])
@cli.command()
def status(): subprocess.run(['liquibase', 'status'])
if __name__ == '__main__': cli()
