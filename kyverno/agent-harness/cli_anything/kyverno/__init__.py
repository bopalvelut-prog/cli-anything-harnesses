import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def apply(): subprocess.run(['kyverno', 'apply', '.'])
@cli.command()
def test(): subprocess.run(['kyverno', 'test', '.'])
if __name__ == '__main__': cli()
