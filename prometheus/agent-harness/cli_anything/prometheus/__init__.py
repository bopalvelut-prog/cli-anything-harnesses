
import click, requests, json
@click.group()
def cli(): pass
PROM = 'http://localhost:9090'
@cli.command()
@click.argument('query')
def query(query): r = requests.get(f'{PROM}/api/v1/query', params={'query': query}); click.echo(json.dumps(r.json()))
@cli.command()
def targets():
    r = requests.get(f'{PROM}/api/v1/targets')
    for t in r.json()['data']['activeTargets']: click.echo(f"{t['labels']['job']} {t['health']}")
if __name__ == '__main__': cli()
