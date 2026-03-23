import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('extend running')
@cli.command()
def start(): click.echo('extend started')
if __name__ == '__main__': cli()
