
import click, requests, json, os

API = os.getenv('HA_URL', 'http://localhost:8123')
TOKEN = os.getenv('HA_TOKEN', '')

@click.group()
def cli(): pass

def headers():
    return {'Authorization': f'Bearer {TOKEN}'} if TOKEN else {}

@cli.command()
def states():
    r = requests.get(f'{API}/api/states', headers=headers())
    states = r.json()
    for s in states:
        click.echo(f"{s['entity_id']}: {s['state']}")

@cli.command()
@click.argument('entity_id')
def state(entity_id):
    r = requests.get(f'{API}/api/states/{entity_id}', headers=headers())
    if r.status_code == 200:
        s = r.json()
        click.echo(f"{s['entity_id']}: {s['state']}")
    else:
        click.echo(f'Not found: {entity_id}')

@cli.command()
@click.argument('entity_id')
@click.argument('state')
@click.option('--attributes', default='{}')
def set_state(entity_id, state, attributes):
    data = {'state': state, 'attributes': json.loads(attributes)}
    r = requests.post(f'{API}/api/services/homeassistant/turn_on', headers=headers(), json=data)
    click.echo(f'Set {entity_id} to {state}')

@cli.command()
@click.argument('message')
def notify(message):
    data = {'message': message}
    r = requests.post(f'{API}/api/services/notify/persistent_notification', headers=headers(), json=data)
    click.echo(f'Notification sent')

if __name__ == '__main__':
    cli()
