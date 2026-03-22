import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def test(): subprocess.run(['vitest'])
@cli.command()
def coverage(): subprocess.run(['vitest', '--coverage'])
@cli.command()
def ui(): subprocess.run(['vitest', '--ui'])
if __name__ == '__main__': cli()
