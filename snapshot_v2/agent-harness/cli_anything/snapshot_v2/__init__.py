import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('snapshot_v2 running')
@cli.command()
def start(): click.echo('snapshot_v2 started')
if __name__ == '__main__': cli()
