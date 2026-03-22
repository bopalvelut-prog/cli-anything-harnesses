
import click, subprocess, json, os

@click.group()
def cli(): pass

@cli.command()
@click.argument('path')
@click.option('--folder', is_flag=True)
def open(path, folder):
    if folder:
        subprocess.run(['code', '--folder-uri', path])
    else:
        subprocess.run(['code', path])
    click.echo(f'Opened: {path}')

@cli.command()
@click.argument('query')
def search(query):
    subprocess.run(['code', '--search', query])
    click.echo(f'Searched: {query}')

@cli.command()
def extensions():
    subprocess.run(['code', '--list-extensions'])

if __name__ == '__main__':
    cli()
