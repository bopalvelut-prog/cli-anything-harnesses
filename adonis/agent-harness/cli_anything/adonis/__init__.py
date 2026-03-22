import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def serve(): subprocess.run(['node', 'ace', 'serve:dev'])
@cli.command()
def migrate(): subprocess.run(['node', 'ace', 'migration:run'])
if __name__ == '__main__': cli()
