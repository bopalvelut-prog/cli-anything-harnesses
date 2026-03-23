import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('pelias running')
@cli.command()
def start(): click.echo('pelias started')
if __name__ == '__main__': cli()
