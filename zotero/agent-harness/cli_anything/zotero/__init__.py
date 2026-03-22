
import click, requests, json, os
@click.group()
def cli(): pass
ZOTERO = os.getenv('ZOTERO_API_KEY', '')
USER = os.getenv('ZOTERO_USER_ID', '')
@cli.command()
def items():
    if not ZOTERO or not USER: click.echo('Set ZOTERO_API_KEY and ZOTERO_USER_ID'); return
    r = requests.get(f'https://api.zotero.org/users/{USER}/items', headers={'Zotero-API-Key': ZOTERO})
    for item in r.json(): click.echo(item['data'].get('title', 'Untitled'))
if __name__ == '__main__': cli()
