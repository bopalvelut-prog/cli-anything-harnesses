import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def run(): subprocess.run(['sbt', 'run'])
@cli.command()
def test(): subprocess.run(['sbt', 'test'])
@cli.command()
def compile(): subprocess.run(['sbt', 'compile'])
if __name__ == '__main__': cli()
