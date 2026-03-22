import click, subprocess
@click.group()
def cli(): pass
@cli.command()
@click.argument('path')
def type(path): subprocess.run(['file', path])
if __name__ == '__main__': cli()
