import click, subprocess
@click.group()
def cli(): pass
@cli.command()
@click.argument('file')
def dump(file): subprocess.run(['xxd', file])
@cli.command()
@click.argument('file')
def reverse(file): subprocess.run(['xxd', '-r', file])
if __name__ == '__main__': cli()
