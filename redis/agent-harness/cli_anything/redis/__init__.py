
import click, redis, json
@click.group()
def cli(): pass
def r(): return redis.Redis(host='localhost', port=6379, decode_responses=True)
@cli.command()
@click.argument('key')
def get(key): click.echo(r().get(key))
@cli.command()
@click.argument('key')
@click.argument('value')
def set(key, value): r().set(key, value); click.echo('OK')
@cli.command()
def keys():
    for k in r().keys(): click.echo(k)
if __name__ == '__main__': cli()
