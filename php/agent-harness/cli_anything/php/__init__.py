import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def serve(): subprocess.run(['php', '-S', 'localhost:8000'])
@cli.command()
def composer(): subprocess.run(['composer', 'install'])
@cli.command()
def test(): subprocess.run(['phpunit'])
if __name__ == '__main__': cli()
