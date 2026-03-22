import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def compile(): subprocess.run(['truffle', 'compile'])
@cli.command()
def migrate(): subprocess.run(['truffle', 'migrate'])
@cli.command()
def test(): subprocess.run(['truffle', 'test'])
if __name__ == '__main__': cli()
