import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('leveldb running')
@cli.command()
def start(): click.echo('leveldb started')
if __name__ == '__main__': cli()
