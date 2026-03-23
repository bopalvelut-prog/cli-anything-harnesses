import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('thinking running')
@cli.command()
def start(): click.echo('thinking started')
if __name__ == '__main__': cli()
