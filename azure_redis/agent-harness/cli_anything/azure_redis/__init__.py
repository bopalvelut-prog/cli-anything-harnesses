import click
@click.group()
def cli(): pass
@cli.command()
def list(): click.echo('Redis list')
@cli.command()
def keys(): click.echo('Redis keys')
if __name__ == '__main__': cli()
