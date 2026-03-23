import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('loopy running')
@cli.command()
def start(): click.echo('loopy started')
if __name__ == '__main__': cli()
