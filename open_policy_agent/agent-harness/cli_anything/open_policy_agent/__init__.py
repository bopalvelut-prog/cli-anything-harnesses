import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def eval(): subprocess.run(['opa', 'eval', '-d', '.', '-i', 'input.json'])
@cli.command()
def test(): subprocess.run(['opa', 'test', '.'])
if __name__ == '__main__': cli()
