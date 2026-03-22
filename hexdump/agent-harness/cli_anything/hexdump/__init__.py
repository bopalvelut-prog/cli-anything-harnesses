import click, subprocess
@click.group()
def cli(): pass
@cli.command()
@click.argument('file')
def dump(file): subprocess.run(['hexdump', '-C', file])
if __name__ == '__main__': cli()
