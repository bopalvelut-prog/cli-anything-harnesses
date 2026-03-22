import click, subprocess
@click.group()
def cli(): pass
@cli.command()
@click.argument('binary')
def analyze(binary): subprocess.run(['r2', binary])
if __name__ == '__main__': cli()
