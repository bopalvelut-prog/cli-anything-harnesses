import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('twelve running')
@cli.command()
def start(): click.echo('twelve started')
if __name__ == '__main__': cli()
