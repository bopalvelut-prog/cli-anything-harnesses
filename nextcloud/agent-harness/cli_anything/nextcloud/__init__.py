
import click, requests, json, os
@click.group()
def cli(): pass
NC = os.getenv('NEXTCLOUD_URL', 'http://localhost')
USER = os.getenv('NEXTCLOUD_USER', '')
PWD = os.getenv('NEXTCLOUD_PWD', '')
@cli.command()
def files():
    r = requests.request('PROPFIND', f'{NC}/remote.php/dav/files/{USER}/', auth=(USER, PWD))
    click.echo(r.text)
if __name__ == '__main__': cli()
