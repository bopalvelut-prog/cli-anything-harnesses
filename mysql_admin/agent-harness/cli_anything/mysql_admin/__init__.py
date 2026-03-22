import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): subprocess.run(['mysqladmin', 'status'])
@cli.command()
def version(): subprocess.run(['mysqladmin', 'version'])
if __name__ == '__main__': cli()
