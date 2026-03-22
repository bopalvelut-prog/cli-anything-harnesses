
import click, requests, json
@click.group()
def cli(): pass
ES = 'http://localhost:9200'
@cli.command()
def health(): r = requests.get(f'{ES}'); click.echo(r.json()['status'])
@cli.command()
@click.argument('index')
def count(index): r = requests.get(f'{ES}/{index}/_count'); click.echo(r.json()['count'])
@cli.command()
@click.argument('index')
@click.argument('query')
def search(index, query):
    r = requests.post(f'{ES}/{index}/_search', json=json.loads(query))
    for h in r.json()['hits']['hits']: click.echo(json.dumps(h['_source']))
if __name__ == '__main__': cli()
