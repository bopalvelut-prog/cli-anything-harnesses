import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('kazoo running')
@cli.command()
def start(): click.echo('kazoo started')
if __name__ == '__main__': cli()
