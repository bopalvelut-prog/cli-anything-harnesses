import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('quota running')
@cli.command()
def start(): click.echo('quota started')
if __name__ == '__main__': cli()
