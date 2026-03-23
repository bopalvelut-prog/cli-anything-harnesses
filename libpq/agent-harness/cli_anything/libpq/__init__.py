import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('libpq running')
@cli.command()
def start(): click.echo('libpq started')
if __name__ == '__main__': cli()
