import click, subprocess
@click.group()
def cli(): pass
@cli.command()
@click.argument('file')
@click.argument('filter', default='. ')
def query(file, filter): subprocess.run(['jq', filter, file])
@cli.command()
@click.argument('file')
def keys(file): subprocess.run(['jq', 'keys', file])
if __name__ == '__main__': cli()
