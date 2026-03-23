import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('regulation running')
@cli.command()
def start(): click.echo('regulation started')
if __name__ == '__main__': cli()
