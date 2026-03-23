import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('mongos running')
@cli.command()
def start(): click.echo('mongos started')
if __name__ == '__main__': cli()
