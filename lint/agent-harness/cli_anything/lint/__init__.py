import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def check(): subprocess.run(['npm', 'run', 'lint'])
@cli.command()
def fix(): subprocess.run(['npm', 'run', 'lint', '--fix'])
if __name__ == '__main__': cli()
