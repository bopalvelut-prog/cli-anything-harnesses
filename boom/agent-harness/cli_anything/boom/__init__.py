import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('boom running')
@cli.command()
def start(): click.echo('boom started')
if __name__ == '__main__': cli()
