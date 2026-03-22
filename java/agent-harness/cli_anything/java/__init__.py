import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def compile(): subprocess.run(['javac', 'Main.java'])
@cli.command()
def run(): subprocess.run(['java', 'Main'])
@cli.command()
@click.argument('args', nargs=-1)
def maven(args): subprocess.run(['mvn'] + list(args))
if __name__ == '__main__': cli()
