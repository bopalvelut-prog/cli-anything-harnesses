import click, subprocess
@click.group()
def cli(): pass
@cli.command()
@click.argument('file')
def scan(file): subprocess.run(['binwalk', file])
@cli.command()
@click.argument('file')
def extract(file): subprocess.run(['binwalk', '-e', file])
if __name__ == '__main__': cli()
