import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): subprocess.run(['nodetool', 'status'])
@cli.command()
def info(): subprocess.run(['nodetool', 'info'])
if __name__ == '__main__': cli()
