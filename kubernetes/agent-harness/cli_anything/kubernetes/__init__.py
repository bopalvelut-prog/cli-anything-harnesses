
import click, os
from kubernetes import client, config
@click.group()
def cli(): pass
try: config.load_kube_config()
except: config.load_incluster_config()
api = client.CoreV1Api()
@cli.command()
def pods():
    for p in api.list_pod_for_all_namespaces().items:
        click.echo(f"{p.metadata.namespace} {p.metadata.name} {p.status.phase}")
@cli.command()
def nodes():
    for n in api.list_node().items:
        click.echo(n.metadata.name)
if __name__ == '__main__': cli()
