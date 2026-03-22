
import click, docker, json
@click.group()
def cli(): pass
client = docker.from_env()
@cli.command()
def ps():
    for c in client.containers.list(): click.echo(f"{c.id[:12]} {c.name} {c.status}")
@cli.command()
@click.argument('image')
def pull(image): client.images.pull(image); click.echo(f'Pulled: {image}')
@cli.command()
@click.argument('name')
def stop(name):
    client.containers.get(name).stop(); click.echo(f'Stopped: {name}')
if __name__ == '__main__': cli()
