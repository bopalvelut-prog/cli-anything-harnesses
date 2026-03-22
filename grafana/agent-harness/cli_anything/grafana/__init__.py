
import click, requests, json, os
@click.group()
def cli(): pass
GF = os.getenv('GRAFANA_URL', 'http://localhost:3000')
TOKEN = os.getenv('GRAFANA_TOKEN', '')
@cli.command()
def datasources():
    h = {'Authorization': f'Bearer {TOKEN}'}
    r = requests.get(f'{GF}/api/datasources', headers=h)
    for d in r.json(): click.echo(f"{d['uid']} {d['type']}")
@cli.command()
def dashboards():
    h = {'Authorization': f'Bearer {TOKEN}'}
    r = requests.get(f'{GF}/api/search', headers=h)
    for d in r.json(): click.echo(f"{d['uid']} {d['title']}")
if __name__ == '__main__': cli()
