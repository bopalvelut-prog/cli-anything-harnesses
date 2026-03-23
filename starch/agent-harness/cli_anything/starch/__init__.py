import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('starch running')
@cli.command()
def start(): click.echo('starch started')
if __name__ == '__main__': cli()
