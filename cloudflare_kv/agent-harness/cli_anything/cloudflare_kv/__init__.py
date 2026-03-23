import click
@click.group()
def cli(): pass
@cli.command()
def get(): click.echo('KV get')
@cli.command()
def put(): click.echo('KV put')
if __name__ == '__main__': cli()
