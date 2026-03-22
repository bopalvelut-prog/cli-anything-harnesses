import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def validate(): subprocess.run(['vector', 'validate', '/etc/vector/vector.toml'])
@cli.command()
def test(): subprocess.run(['vector', 'test', '/etc/vector/vector.toml'])
@cli.command()
def top(): subprocess.run(['vector', 'top'])
if __name__ == '__main__': cli()
