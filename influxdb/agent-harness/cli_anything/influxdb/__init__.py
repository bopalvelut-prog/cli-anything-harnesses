
import click, os
from influxdb_client import InfluxDBClient
@click.group()
def cli(): pass
client = InfluxDBClient(url=os.getenv('INFLUX_URL','http://localhost:8086'), token=os.getenv('INFLUX_TOKEN',''))
@cli.command()
def buckets():
    for b in client.buckets_api().find_buckets().buckets: click.echo(b.name)
@cli.command()
@click.argument('org')
@click.argument('query')
def query(org, query):
    q = client.query_api(); r = q.query(query, org=org)
    for t in r: click.echo(t)
if __name__ == '__main__': cli()
