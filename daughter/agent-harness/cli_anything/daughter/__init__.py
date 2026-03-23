import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('daughter running')
@cli.command()
def start(): click.echo('daughter started')
if __name__ == '__main__': cli()
