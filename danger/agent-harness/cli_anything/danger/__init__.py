import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('danger running')
@cli.command()
def start(): click.echo('danger started')
if __name__ == '__main__': cli()
