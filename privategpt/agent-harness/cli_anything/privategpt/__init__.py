import click
@click.group()
def cli(): pass
@cli.command()
def start(): click.echo('PrivateGPT start')
@cli.command()
def ingest(): click.echo('PrivateGPT ingest')
if __name__ == '__main__': cli()
