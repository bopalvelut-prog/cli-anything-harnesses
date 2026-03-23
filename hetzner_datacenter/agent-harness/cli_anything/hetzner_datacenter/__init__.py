import click
@click.group()
def cli(): pass
@cli.command()
def list(): click.echo('Datacenters')
if __name__ == '__main__': cli()
