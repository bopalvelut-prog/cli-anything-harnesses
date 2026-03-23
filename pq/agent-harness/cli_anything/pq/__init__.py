import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('pq running')
@cli.command()
def start(): click.echo('pq started')
if __name__ == '__main__': cli()
