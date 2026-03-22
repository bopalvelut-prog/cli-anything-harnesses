import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def serve(): subprocess.run(['craft', 'serve'])
@cli.command()
def migrate(): subprocess.run(['craft', 'migrate/all'])
if __name__ == '__main__': cli()
