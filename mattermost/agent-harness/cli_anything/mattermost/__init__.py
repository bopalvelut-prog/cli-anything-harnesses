
import click, requests, json, os
@click.group()
def cli(): pass
MM = os.getenv('MATTERMOST_URL', 'http://localhost:8065')
TOKEN = os.getenv('MATTERMOST_TOKEN', '')
@cli.command()
def channels():
    h = {'Authorization': f'Bearer {TOKEN}', 'Content-Type': 'application/json'}
    r = requests.get(f'{MM}/api/v4/channels', headers=h)
    for c in r.json(): click.echo(f"{c['id']} {c['name']}")
@cli.command()
@click.argument('channel_id')
@click.argument('message')
def post(channel_id, message):
    h = {'Authorization': f'Bearer {TOKEN}', 'Content-Type': 'application/json'}
    requests.post(f'{MM}/api/v4/posts', headers=h, json={'channel_id': channel_id, 'message': message})
    click.echo('Posted')
if __name__ == '__main__': cli()
