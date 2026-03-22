import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def test(): subprocess.run(['npx', 'playwright', 'test'])
@cli.command()
def ui(): subprocess.run(['npx', 'playwright', 'test', '--ui'])
@cli.command()
def show(): subprocess.run(['npx', 'playwright', 'show-report'])
if __name__ == '__main__': cli()
