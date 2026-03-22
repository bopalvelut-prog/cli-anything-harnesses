import click, subprocess
@click.group()
def cli(): pass
@cli.command()
@click.argument('file')
@click.argument('filter', default='. ')
def query(file, filter): subprocess.run(['yq', filter, file])
@cli.command()
@click.argument('file')
def to_json(file): subprocess.run(['yq', '-o=json', '.', file])
if __name__ == '__main__': cli()
