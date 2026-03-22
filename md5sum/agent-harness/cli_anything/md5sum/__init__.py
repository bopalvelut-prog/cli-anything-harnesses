import click, subprocess
@click.group()
def cli(): pass
@cli.command()
@click.argument('file')
def hash(file): subprocess.run(['md5sum', file])
if __name__ == '__main__': cli()
