import click, subprocess
@click.group()
def cli(): pass
@cli.command()
@click.argument('file')
def encrypt(file): subprocess.run(['gpg', '-c', file])
@cli.command()
@click.argument('file')
def decrypt(file): subprocess.run(['gpg', '-d', file])
@cli.command()
def list(): subprocess.run(['gpg', '--list-keys'])
if __name__ == '__main__': cli()
