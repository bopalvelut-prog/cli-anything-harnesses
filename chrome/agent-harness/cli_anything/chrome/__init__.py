
import click, subprocess
@click.group()
def cli(): pass
@cli.command()
@click.argument('url')
@click.option('--incognito', is_flag=True)
def open(url, incognito):
    cmd = ['google-chrome'] + (['--incognito'] if incognito else []) + [url]
    subprocess.run(cmd); click.echo(f'Opened: {url}')
if __name__ == '__main__': cli()
