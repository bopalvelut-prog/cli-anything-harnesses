import click, subprocess
@click.group()
def cli(): pass
@cli.command()
@click.argument('file')
def extract(file): subprocess.run(['strings', file])
if __name__ == '__main__': cli()
