import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def run(): subprocess.run(['kotlin', 'MainKt'])
@cli.command()
def compile(): subprocess.run(['kotlinc', 'Main.kt'])
if __name__ == '__main__': cli()
