import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def develop(): subprocess.run(['medusa', 'develop'])
@cli.command()
def migrations(): subprocess.run(['medusa', 'migrations', 'run'])
if __name__ == '__main__': cli()
