import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('stale running')
@cli.command()
def start(): click.echo('stale started')
if __name__ == '__main__': cli()
