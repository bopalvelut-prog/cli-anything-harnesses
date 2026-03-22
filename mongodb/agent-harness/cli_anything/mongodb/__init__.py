
import click, pymongo, json, os
@click.group()
def cli(): pass
client = pymongo.MongoClient(os.getenv('MONGO_URL', 'mongodb://localhost:27017'))
@cli.command()
@click.argument('db')
def collections(db):
    for c in client[db].list_collection_names(): click.echo(c)
@cli.command()
@click.argument('db')
@click.argument('coll')
@click.argument('query', default='{}')
def find(db, coll, query):
    docs = list(client[db][coll].find(json.loads(query)))
    click.echo(json.dumps(docs, default=str))
if __name__ == '__main__': cli()
