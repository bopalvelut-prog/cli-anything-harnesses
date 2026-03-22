
import click, requests, json, os

API = os.getenv('SYNCTHING_URL', 'http://localhost:8384')
KEY = os.getenv('SYNCTHING_KEY', '')

@click.group()
def cli(): pass

def headers():
    return {'X-API-Key': KEY} if KEY else {}

@cli.command()
def status():
    r = requests.get(f'{API}/rest/system/ping', headers=headers(), verify=False)
    if r.status_code == 200:
        click.echo('Syncthing is running')
    else:
        click.echo('Syncthing not reachable')

@cli.command()
def folders():
    r = requests.get(f'{API}/rest/config/folders', headers=headers(), verify=False)
    folders = r.json()
    for f in folders:
        click.echo(f"{f['id']}: {f.get('path', 'N/A')}")

@cli.command()
def devices():
    r = requests.get(f'{API}/rest/config/devices', headers=headers(), verify=False)
    devices = r.json()
    for d in devices:
        click.echo(f"{d['deviceID'][:8]}...: {d.get('name', 'unknown')}")

@cli.command()
def connections():
    r = requests.get(f'{API}/rest/system/connections', headers=headers(), verify=False)
    click.echo(json.dumps(r.json(), indent=2))

if __name__ == '__main__':
    cli()
