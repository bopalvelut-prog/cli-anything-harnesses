import click, subprocess
@click.group()
def cli(): pass
@cli.command()
@click.argument('file')
def encrypt(file): subprocess.run(['age', '-o', file + '.age', file])
@cli.command()
@click.argument('file')
def decrypt(file): subprocess.run(['age', '-d', file])
if __name__ == '__main__': cli()
