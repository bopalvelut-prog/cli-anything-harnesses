import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('turbopack running')
@cli.command()
def start(): click.echo('turbopack started')
if __name__ == '__main__': cli()
